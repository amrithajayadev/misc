grid = [[0, 0, 0, 0],
        [0, 0, "x", 0],
        [0, "x", 0, 0],
        ["x", 0, 0, 0]]


def find_path(grid, r, c, rows, cols):
    if r == rows and c == cols:
        return True
    if r <= rows and grid[r][c] != "x" and c <= cols:
        return find_path(grid, r + 1, c, rows, cols) or find_path(grid, r, c + 1, rows, cols)
    return False


r = find_path(grid, 0, 0, len(grid) - 1, len(grid[0]) - 1)
if r:
    print("There is a path")
else:
    print("No path")


