# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def create_cnf(n, m, edges):
    clauses = []
    
    # Each vertex must have at least one color
    for i in range(1, n + 1):
        clauses.append([3 * (i - 1) + 1, 3 * (i - 1) + 2, 3 * (i - 1) + 3])
    
    # Each vertex can have at most one color
    for i in range(1, n + 1):
        clauses.append([- (3 * (i - 1) + 1), - (3 * (i - 1) + 2)])
        clauses.append([- (3 * (i - 1) + 1), - (3 * (i - 1) + 3)])
        clauses.append([- (3 * (i - 1) + 2), - (3 * (i - 1) + 3)])
    
    # Adjacent vertices must have different colors
    for (u, v) in edges:
        clauses.append([- (3 * (u - 1) + 1), - (3 * (v - 1) + 1)])
        clauses.append([- (3 * (u - 1) + 2), - (3 * (v - 1) + 2)])
        clauses.append([- (3 * (u - 1) + 3), - (3 * (v - 1) + 3)])
    
    # Output the number of clauses and variables
    num_clauses = len(clauses)
    num_vars = 3 * n
    print(num_clauses, num_vars)
    
    # Output each clause
    for clause in clauses:
        print(" ".join(map(str, clause)) + " 0")
create_cnf(n, m, edges)
