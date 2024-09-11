#Uses python3

import sys

def dfs(adj, visited, order, x):
    visited[x] = True
    for neighbor in adj[x]:
        if not visited[neighbor]:
            dfs(adj, visited, order, neighbor)
    order.append(x)

def toposort(adj):
    n = len(adj)
    visited = [False] * n
    order = []
    for i in range(n):
        if not visited[i]:
            dfs(adj, visited, order, i)
    return order[::-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

