#Uses python3

import sys


def number_of_components(adj):
    def dfs(v):
        stack = [v]
        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

    n = len(adj)
    visited = [False] * n
    num_components = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            num_components += 1

    return num_components

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
