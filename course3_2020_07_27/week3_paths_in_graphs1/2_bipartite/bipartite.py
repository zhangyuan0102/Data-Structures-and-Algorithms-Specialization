#Uses python3

import sys
import queue
from collections import deque
def bipartite(adj):
    n = len(adj)
    color = [-1] * n 

    def bfs(s):
        queue = deque([s])
        color[s] = 0  
        while queue:
            u = queue.popleft()
            for neighbor in adj[u]:
                if color[neighbor] == -1: 
                    queue.append(neighbor)
                    color[neighbor] = 1 - color[u]  
                elif color[neighbor] == color[u]: 
                    return False
        return True

    for i in range(n):
        if color[i] == -1:  
            if not bfs(i):
                return 0  
    return 1 

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
    print(bipartite(adj))
