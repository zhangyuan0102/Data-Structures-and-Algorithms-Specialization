#python3
def find_eulerian_cycle(n, m, edges):
    from collections import defaultdict, deque
    
    # Create adjacency list and degree counts
    out_deg = [0] * (n + 1)
    in_deg = [0] * (n + 1)
    adj_list = defaultdict(list)
    
    for u, v in edges:
        adj_list[u].append(v)
        out_deg[u] += 1
        in_deg[v] += 1

    # Check if all vertices have equal in-degree and out-degree
    for i in range(1, n + 1):
        if in_deg[i] != out_deg[i]:
            return 0, []

    # Hierholzer's algorithm to find Eulerian cycle
    def hierholzer(start_node):
        cycle = []
        stack = [start_node]
        while stack:
            v = stack[-1]
            if adj_list[v]:
                next_v = adj_list[v].pop()
                stack.append(next_v)
            else:
                cycle.append(stack.pop())
        cycle.reverse()
        return cycle

    # Start from any vertex with an outgoing edge
    start_vertex = 1
    for i in range(1, n + 1):
        if out_deg[i] > 0:
            start_vertex = i
            break
    
    cycle = hierholzer(start_vertex)
    
    # Verify if the cycle contains all edges
    if len(cycle) != m + 1:
        return 0, []

    return 1, cycle

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
edges = []

index = 2
for _ in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    edges.append((u, v))
    index += 2

result, cycle = find_eulerian_cycle(n, m, edges)

# Print the result
if result == 0:
    print(0)
else:
    print(1)
    print(" ".join(map(str, cycle[:-1]))) 