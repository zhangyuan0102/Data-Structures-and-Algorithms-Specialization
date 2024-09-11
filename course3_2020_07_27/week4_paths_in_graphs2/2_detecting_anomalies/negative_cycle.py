#Uses python3

import sys


def negative_cycle(adj, cost):
    n = len(adj)
    distances = [float('inf')] * n
    distances[0] = 0

    # Relax edges up to n times to detect negative weight cycles
    for _ in range(n):
        for u in range(n):
            for i, v in enumerate(adj[u]):
                if distances[u] != float('inf') and distances[u] + cost[u][i] < distances[v]:
                    distances[v] = distances[u] + cost[u][i]
                    # If we are in the n-th iteration and we can still relax an edge,
                    # it means there is a negative weight cycle.
                    if _ == n - 1:
                        return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
