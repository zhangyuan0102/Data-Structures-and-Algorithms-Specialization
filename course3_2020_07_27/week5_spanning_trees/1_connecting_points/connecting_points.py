#Uses python3
import sys
import math
import heapq

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def minimum_distance(x, y):
    n = len(x)
    result = 0.0

    # Initialize visited set and min-heap
    visited = [False] * n
    min_heap = [(0, 0)]  # (distance, vertex)
    total_distance = 0.0

    while min_heap:
        dist, u = heapq.heappop(min_heap)

        if visited[u]:
            continue

        total_distance += dist
        visited[u] = True

        for v in range(n):
            if not visited[v]:
                heapq.heappush(min_heap, (calculate_distance(x[u], y[u], x[v], y[v]), v))

    return total_distance


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
