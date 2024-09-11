#Uses python3

import sys

sys.setrecursionlimit(200000)

def dfs(adj, visited, order, v):
    visited[v] = True
    for neighbor in adj[v]:
        if not visited[neighbor]:
            dfs(adj, visited, order, neighbor)
    order.append(v)

def reverse_graph(adj):
    n = len(adj)
    adj_r = [[] for _ in range(n)]
    for v in range(n):
        for neighbor in adj[v]:
            adj_r[neighbor].append(v)
    return adj_r

def dfs_for_scc(adj, visited, v):
    visited[v] = True
    for neighbor in adj[v]:
        if not visited[neighbor]:
            dfs_for_scc(adj, visited, neighbor)

def number_of_strongly_connected_components(adj):
    n = len(adj)
    visited = [False] * n
    order = []
    
    for i in range(n):
        if not visited[i]:
            dfs(adj, visited, order, i)
    
    adj_r = reverse_graph(adj)
    
    visited = [False] * n
    scc_count = 0
    while order:
        v = order.pop()
        if not visited[v]:
            dfs_for_scc(adj_r, visited, v)
            scc_count += 1
    
    return scc_count
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
