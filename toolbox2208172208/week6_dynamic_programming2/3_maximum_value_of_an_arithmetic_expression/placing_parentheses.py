def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def maximum_value(dataset):
    # Split the dataset into numbers and operators
    numbers = []
    operators = []
    i = 0
    while i < len(dataset):
        if dataset[i].isdigit():
            j = i
            while j < len(dataset) and dataset[j].isdigit():
                j += 1
            numbers.append(int(dataset[i:j]))
            i = j
        else:
            operators.append(dataset[i])
            i += 1
    
    n = len(numbers)
    
    # Initialize dp tables
    dp_max = [[0] * n for _ in range(n)]
    dp_min = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp_max[i][i] = numbers[i]
        dp_min[i][i] = numbers[i]
    
    # Fill dp tables
    for l in range(2, n + 1):  # l is the length of the interval
        for i in range(0, n - l + 1):
            j = i + l - 1
            dp_max[i][j] = float('-inf')
            dp_min[i][j] = float('inf')
            for k in range(i, j):
                # Operator between k and k+1
                op = operators[k]
                
                a = evaluate(dp_max[i][k], dp_max[k + 1][j], op)
                b = evaluate(dp_max[i][k], dp_min[k + 1][j], op)
                c = evaluate(dp_min[i][k], dp_max[k + 1][j], op)
                d = evaluate(dp_min[i][k], dp_min[k + 1][j], op)
                
                dp_max[i][j] = max(dp_max[i][j], a, b, c, d)
                dp_min[i][j] = min(dp_min[i][j], a, b, c, d)
    
    return dp_max[0][n - 1]


if __name__ == "__main__":
    print(maximum_value(input()))
