#python3
import sys

def parse_input():
    data = sys.stdin.read().strip().split('\n')
    pieces = []
    for d in data:
        pieces.append(d[1:-1].split(','))
    print("Parsed pieces:", pieces)  # Debug print
    return pieces

def classify_pieces(pieces):
    corners = []
    edges = []
    inner = []
    for piece in pieces:
        black_count = piece.count('black')
        if black_count == 2:
            corners.append(piece)
        elif black_count == 1:
            edges.append(piece)
        else:
            inner.append(piece)
    print("Corners:", corners)  # Debug print
    print("Edges:", edges)  # Debug print
    print("Inner pieces:", inner)  # Debug print
    return corners, edges, inner

def place_corners_and_edges(corners, edges):
    grid = [[None for _ in range(5)] for _ in range(5)]

    # Place corners
    for corner in corners:
        if corner[0] == 'black' and corner[1] == 'black':
            grid[0][0] = corner
        elif corner[0] == 'black' and corner[3] == 'black':
            grid[0][4] = corner
        elif corner[2] == 'black' and corner[1] == 'black':
            grid[4][0] = corner
        elif corner[2] == 'black' and corner[3] == 'black':
            grid[4][4] = corner

    # Place edges
    for edge in edges:
        if edge[0] == 'black':
            for col in range(1, 4):
                if grid[0][col] is None:
                    grid[0][col] = edge
                    break
        elif edge[2] == 'black':
            for col in range(1, 4):
                if grid[4][col] is None:
                    grid[4][col] = edge
                    break
        elif edge[1] == 'black':
            for row in range(1, 4):
                if grid[row][0] is None:
                    grid[row][0] = edge
                    break
        elif edge[3] == 'black':
            for row in range(1, 4):
                if grid[row][4] is None:
                    grid[row][4] = edge
                    break

    print("Grid after placing corners and edges:")
    for row in grid:
        print(row)  # Debug print
    return grid

def can_place(piece, grid, row, col):
    if row > 0 and grid[row-1][col] and grid[row-1][col][2] != piece[0]:
        return False
    if col > 0 and grid[row][col-1] and grid[row][col-1][3] != piece[1]:
        return False
    if row < 4 and grid[row+1][col] and grid[row+1][col][0] != piece[2]:
        return False
    if col < 4 and grid[row][col+1] and grid[row][col+1][1] != piece[3]:
        return False
    return True

def solve(grid, inner, index):
    if index == len(inner):
        return True
    for row in range(1, 4):
        for col in range(1, 4):
            if grid[row][col] is None:
                for i, piece in enumerate(inner):
                    if piece:
                        inner[i] = None
                        if can_place(piece, grid, row, col):
                            grid[row][col] = piece
                            print("Placing piece:", piece, "at", (row, col))  # Debug print
                            if solve(grid, inner, index + 1):
                                return True
                            grid[row][col] = None
                        inner[i] = piece
                return False
    return False

def main():
    pieces = parse_input()
    corners, edges, inner = classify_pieces(pieces)
    grid = place_corners_and_edges(corners, edges)
    if solve(grid, inner, 0):
        for i in range(5):
            print(';'.join(['(' + ','.join(grid[i][j]) + ')' for j in range(5)]))
    else:
        print("No solution found")

if __name__ == "__main__":
    main()

