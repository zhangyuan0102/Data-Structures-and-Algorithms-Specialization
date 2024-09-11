#Uses python3

import sys


def acyclic(adj):
    def dfs(v):
        visited[v] = True
        recursion_stack[v] = True
        for neighbor in adj[v]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif recursion_stack[neighbor]:
                return True
        recursion_stack[v] = False
        return False

    n = len(adj)
    visited = [False] * n
    recursion_stack = [False] * n

    for i in range(n):
        if not visited[i]:
            if dfs(i):
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
