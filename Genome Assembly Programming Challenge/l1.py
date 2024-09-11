#python3
from collections import deque, defaultdict

class MaxFlowEdmondsKarp:
    def __init__(self, n):
        self.n = n
        self.capacity = defaultdict(lambda: defaultdict(int))
        self.flow = defaultdict(lambda: defaultdict(int))

    def add_edge(self, u, v, capacity):
        self.capacity[u][v] += capacity
        self.capacity[v][u] += 0  # Ensure the reverse edge exists in the capacity graph

    def bfs(self, source, sink, parent):
        visited = [False] * self.n
        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()

            for v in self.capacity[u]:
                if not visited[v] and self.capacity[u][v] - self.flow[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True

        return False

    def edmonds_karp(self, source, sink):
        parent = [-1] * self.n
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.capacity[parent[s]][s] - self.flow[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink

            while v != source:
                u = parent[v]
                self.flow[u][v] += path_flow
                self.flow[v][u] -= path_flow
                v = parent[v]

        return max_flow

def circulation_problem(n, m, edges):
    source = n
    sink = n + 1
    max_flow_solver = MaxFlowEdmondsKarp(n + 2)
    supply = [0] * n
    demand = [0] * n

    for u, v, l, c in edges:
        u -= 1
        v -= 1
        max_flow_solver.add_edge(u, v, c - l)
        supply[u] -= l
        demand[v] += l

    total_demand = 0
    for i in range(n):
        if demand[i] > 0:
            max_flow_solver.add_edge(source, i, demand[i])
            total_demand += demand[i]
        if supply[i] < 0:
            max_flow_solver.add_edge(i, sink, -supply[i])

    max_flow = max_flow_solver.edmonds_karp(source, sink)

    if max_flow != total_demand:
        return "NO"

    result = ["YES"]
    flow = []
    for u, v, l, c in edges:
        u -= 1
        v -= 1
        flow.append(max_flow_solver.flow[u][v] + l)
    
    result.extend(map(str, flow))
    return "\n".join(result)

# Input reading
n, m = map(int, input().strip().split())
edges = []
for _ in range(m):
    u, v, l, c = map(int, input().strip().split())
    edges.append((u, v, l, c))

# Solve the problem
result = circulation_problem(n, m, edges)
print(result)

