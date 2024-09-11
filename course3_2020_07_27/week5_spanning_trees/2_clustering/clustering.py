#Uses python3
import sys
import math

class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def clustering(x, y, k):
    n = len(x)
    edges = []
    
    # Create all edges with their distances
    for i in range(n):
        for j in range(i + 1, n):
            dist = calculate_distance(x[i], y[i], x[j], y[j])
            edges.append(Edge(i, j, dist))

    # Sort edges by weight
    edges.sort(key=lambda edge: edge.weight)

    disjoint_set = DisjointSet(n)
    mst_edges = []
    
    # Kruskal's algorithm to find the minimum spanning tree
    for edge in edges:
        if disjoint_set.find(edge.u) != disjoint_set.find(edge.v):
            disjoint_set.union(edge.u, edge.v)
            mst_edges.append(edge)

    # Sort the MST edges by weight in descending order
    mst_edges.sort(key=lambda edge: edge.weight, reverse=True)
    
    # Remove the (k-1) largest edges
    for _ in range(k - 2):
        mst_edges.pop(0)

    # The largest value of d is the smallest edge weight in the remaining MST edges
    return mst_edges[0].weight if mst_edges else 0.0




if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
