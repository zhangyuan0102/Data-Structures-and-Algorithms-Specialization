# python3
import sys
import itertools

INF = 10 ** 9

def read_data():
    input = sys.stdin.read
    data = input().split()
    index = 0
    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1
    graph = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u = int(data[index]) - 1
        index += 1
        v = int(data[index]) - 1
        index += 1
        weight = int(data[index])
        index += 1
        graph[u][v] = graph[v][u] = weight
    return graph

def optimal_path(graph):
    n = len(graph)
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):
                for v in range(n):
                    if mask & (1 << v) == 0:
                        dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + graph[u][v])

    min_cost = min(dp[(1 << n) - 1][i] + graph[i][0] for i in range(n))
    if min_cost >= INF:
        return -1, []

    # Reconstruct the path
    mask = (1 << n) - 1
    last = 0
    for i in range(1, n):
        if dp[mask][i] + graph[i][0] < dp[mask][last] + graph[last][0]:
            last = i

    path = []
    for _ in range(n):
        path.append(last + 1)
        next_mask = mask & ~(1 << last)
        for i in range(n):
            if dp[mask][last] == dp[next_mask][i] + graph[i][last]:
                mask = next_mask
                last = i
                break

    path.reverse()
    return min_cost, path

def print_answer(path_weight, path):
    if path_weight == -1:
        print(path_weight)
    else:
        print(path_weight)
        print(' '.join(map(str, path)))

if __name__ == '__main__':
    print_answer(*optimal_path(read_data()))
