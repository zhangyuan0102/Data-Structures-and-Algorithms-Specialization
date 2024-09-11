# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def create_cnf(n, m, edges):
    clauses = []
    
    # 每个顶点必须出现在路径中的某个位置
    for i in range(1, n + 1):
        clause = [i + n * j for j in range(n)]
        clauses.append(clause)
    
    # 每个顶点只能出现在路径中的一个位置
    for i in range(1, n + 1):
        for j in range(n):
            for k in range(j + 1, n):
                clauses.append([-(i + n * j), -(i + n * k)])
    
    # 每个位置必须被某个顶点占据
    for j in range(n):
        clause = [i + n * j for i in range(1, n + 1)]
        clauses.append(clause)
    
    # 没有两个顶点可以占据路径中的同一个位置
    for j in range(n):
        for i in range(1, n + 1):
            for k in range(i + 1, n + 1):
                clauses.append([-(i + n * j), -(k + n * j)])
    
    # 相邻顶点在路径中必须是相邻的
    edges_set = set((min(u, v), max(u, v)) for u, v in edges)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and (min(i, j), max(i, j)) not in edges_set:
                for k in range(n - 1):
                    clauses.append([-(i + n * k), -(j + n * (k + 1))])
    
    # 输出子句和变量数量
    num_clauses = len(clauses)
    num_vars = n * n
    print(num_clauses, num_vars)
    
    # 输出每个子句
    for clause in clauses:
        print(" ".join(map(str, clause)) + " 0")

create_cnf(n, m, edges)