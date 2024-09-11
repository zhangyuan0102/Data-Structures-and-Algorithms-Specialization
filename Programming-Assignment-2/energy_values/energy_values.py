# python3

EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def SelectPivotElement(a, used_rows, used_columns):
    size = len(a)
    pivot_element = Position(0, 0)

    # Find the first free column
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
    
    # Initialize maximum value and row index for the pivot
    max_value = 0
    for row in range(size):
        if not used_rows[row] and abs(a[row][pivot_element.column]) > max_value:
            max_value = abs(a[row][pivot_element.column])
            pivot_element.row = row
    
    if max_value < EPS:  # If the maximum value is very close to zero
        return None
    
    return pivot_element
def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.row], a[pivot_element.column] = a[pivot_element.column], a[pivot_element.row]
    b[pivot_element.row], b[pivot_element.column] = b[pivot_element.column], b[pivot_element.row]
    used_rows[pivot_element.row], used_rows[pivot_element.column] = used_rows[pivot_element.column], used_rows[pivot_element.row]
    pivot_element.row = pivot_element.column

def ProcessPivotElement(a, b, pivot_element):
    n = len(a)
    pivot_value = a[pivot_element.row][pivot_element.column]

    for i in range(pivot_element.column, n):
        a[pivot_element.row][i] /= pivot_value
    b[pivot_element.row] /= pivot_value

    for i in range(n):
        if i != pivot_element.row:
            factor = a[i][pivot_element.column]
            for j in range(pivot_element.column, n):
                a[i][j] -= factor * a[pivot_element.row][j]
            b[i] -= factor * b[pivot_element.row]

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        if pivot_element is None:
            continue
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)

    return b

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    exit(0)
