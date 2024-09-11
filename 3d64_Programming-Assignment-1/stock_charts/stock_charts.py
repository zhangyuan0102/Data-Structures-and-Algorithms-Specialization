# python3
from collections import deque

class StockCharts:
    def read_data(self):
        n, k = map(int, input().split())
        stock_data = [list(map(int, input().split())) for _ in range(n)]
        return stock_data

    def write_response(self, result):
        print(result)

    def min_charts(self, stock_data):
        n = len(stock_data)

        # Function to determine if stock1 can be placed above stock2
        def can_place_above(stock1, stock2):
            return all(x > y for x, y in zip(stock1, stock2))

        # Build the DAG
        dag = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and can_place_above(stock_data[i], stock_data[j]):
                    dag[i].append(j)

        # Convert DAG to bipartite graph
        bipartite_graph = [[] for _ in range(n)]
        for i in range(n):
            for j in dag[i]:
                bipartite_graph[i].append(j)

        # Use BFS to create layers for Hopcroft-Karp algorithm
        def bfs():
            queue = deque()
            for u in range(n):
                if match_u[u] == -1:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = float('inf')
            found_augmenting_path = False
            while queue:
                u = queue.popleft()
                for v in bipartite_graph[u]:
                    if match_v[v] == -1:
                        found_augmenting_path = True
                    elif dist[match_v[v]] == float('inf'):
                        dist[match_v[v]] = dist[u] + 1
                        queue.append(match_v[v])
            return found_augmenting_path

        # Use DFS to find augmenting paths in layers created by BFS
        def dfs(u):
            for v in bipartite_graph[u]:
                if match_v[v] == -1 or (dist[match_v[v]] == dist[u] + 1 and dfs(match_v[v])):
                    match_u[u] = v
                    match_v[v] = u
                    return True
            dist[u] = float('inf')
            return False

        match_u = [-1] * n
        match_v = [-1] * n
        dist = [-1] * n

        matching_size = 0
        while bfs():
            for u in range(n):
                if match_u[u] == -1:
                    if dfs(u):
                        matching_size += 1

        # The number of charts is the length of DAG minus the size of the maximum matching
        return len(dag) - matching_size

    def solve(self):
        stock_data = self.read_data()
        result = self.min_charts(stock_data)
        self.write_response(result)

if __name__ == '__main__':
    stock_charts = StockCharts()
    stock_charts.solve()