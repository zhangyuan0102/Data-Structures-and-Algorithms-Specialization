#python3
from collections import defaultdict, deque

def build_de_bruijn_graph(kmers):
    graph = defaultdict(list)
    for kmer in kmers:
        prefix = kmer[:-1]
        suffix = kmer[1:]
        graph[prefix].append(suffix)
    return graph

def calculate_degrees(graph):
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    for node in graph:
        out_degree[node] += len(graph[node])
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    return in_degree, out_degree

def find_start_node(graph, in_degree, out_degree):
    start_node = None
    for node in graph:
        if out_degree[node] - in_degree[node] == 1:
            start_node = node
            break
    
    if not start_node:
        start_node = next(iter(graph))
    
    return start_node

def find_eulerian_cycle(graph, start_node):
    path = []
    stack = [start_node]
    current_path = deque()
    
    while stack:
        current = stack[-1]
        if graph[current]:
            next_node = graph[current].pop()
            stack.append(next_node)
        else:
            current_path.appendleft(stack.pop())
    
    path = list(current_path)
    return path

def assemble_genome(path):
    genome = path[0]
    for node in path[1:]:
        genome += node[-1]
    return genome

def main():
    import sys
    input = sys.stdin.read().strip().split()
    kmers = input
    
    graph = build_de_bruijn_graph(kmers)
    in_degree, out_degree = calculate_degrees(graph)
    start_node = find_start_node(graph, in_degree, out_degree)
    path = find_eulerian_cycle(graph, start_node)
    genome = assemble_genome(path)
    
    # Remove the last (k-1) characters to form the circular genome
    k = len(kmers[0])
    circular_genome = genome[:-(k-1)]
    print(circular_genome)

if __name__ == "__main__":
    main()

