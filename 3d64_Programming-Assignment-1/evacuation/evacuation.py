# python3
from collections import deque

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
def bfs(graph, from_, to, parent):
    visited = [False] * graph.size()
    queue = deque([from_])
    visited[from_] = True

    while queue:
        current = queue.popleft()

        for id in graph.get_ids(current):
            edge = graph.get_edge(id)
            if not visited[edge.v] and edge.capacity > edge.flow:
                queue.append(edge.v)
                visited[edge.v] = True
                parent[edge.v] = id
                if edge.v == to:
                    return True

    return False

def max_flow(graph, from_, to):
    flow = 0
    parent = [-1] * graph.size()

    while bfs(graph, from_, to, parent):
        path_flow = float('Inf')
        s = to

        # Find the maximum flow through the path found by BFS
        while s != from_:
            id = parent[s]
            path_flow = min(path_flow, graph.get_edge(id).capacity - graph.get_edge(id).flow)
            s = graph.get_edge(id).u

        flow += path_flow
        v = to

        # Update the flow for each edge and its corresponding backward edge
        while v != from_:
            id = parent[v]
            graph.add_flow(id, path_flow)
            v = graph.get_edge(id).u

    return flow

def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph

if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
