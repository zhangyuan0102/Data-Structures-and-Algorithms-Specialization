#python3
from collections import defaultdict, deque
import sys

def read_reads():
    reads = []
    for _ in range(400):
        reads.append(input().strip())
    return reads

def build_de_bruijn_graph(reads, k):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    for read in reads:
        for i in range(len(read) - k + 1):
            k_mer1 = read[i:i + k - 1]
            k_mer2 = read[i + 1:i + k]
            graph[k_mer1].append(k_mer2)
            out_degree[k_mer1] += 1
            in_degree[k_mer2] += 1
    
    return graph, in_degree, out_degree

def is_eulerian_cycle_possible(graph, in_degree, out_degree):
    start_node = None
    for node in out_degree:
        if out_degree[node] != in_degree[node]:
            return False
        if start_node is None:
            start_node = node
    
    visited = set()
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append(neighbor)
    
    return len(visited) == len(graph)

def find_best_k(reads):
    left, right = 1, 100
    best_k = -1
    
    while left <= right:
        mid = (left + right) // 2
        graph, in_degree, out_degree = build_de_bruijn_graph(reads, mid)
        if is_eulerian_cycle_possible(graph, in_degree, out_degree):
            best_k = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return best_k

if __name__ == "__main__":
    reads = read_reads()
    best_k = find_best_k(reads)
    print(best_k)
