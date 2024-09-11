# python3
from collections import deque
class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def bfs(self, pair_u, pair_v, dist, n):
        queue = deque()
        for u in range(n):
            if pair_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[-1] = float('inf')
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[-1]:
                for v in self.adj[u]:
                    if dist[pair_v[v]] == float('inf'):
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[-1] != float('inf')

    def dfs(self, u, pair_u, pair_v, dist):
        if u != -1:
            for v in self.adj[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if self.dfs(pair_v[v], pair_u, pair_v, dist):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = float('inf')
            return False
        return True

    def find_matching(self, adj_matrix):
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        
        self.adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if adj_matrix[i][j]:
                    self.adj[i].append(j)
        
        pair_u = [-1] * n
        pair_v = [-1] * m
        dist = [-1] * (n + 1)
        
        matching = 0
        while self.bfs(pair_u, pair_v, dist, n):
            for u in range(n):
                if pair_u[u] == -1:
                    if self.dfs(u, pair_u, pair_v, dist):
                        matching += 1
        
        result = [-1] * n
        for u in range(n):
            if pair_u[u] != -1:
                result[u] = pair_u[u]
        return result

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
