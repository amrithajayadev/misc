inp1 = [[0, 0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]]  # works

inp2 = [[1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]]  # works

# inp = [[1, 1, 1, 0, 1, 1, 1],
#  [1, 1, 1, 0, 1, 1, 1],
#  [1, 1, 1, 0, 1, 1, 1],
#  [0, 0, 0, 0, 1, 1, 1],
#  [1, 1, 1, 0, 1, 1, 1]]


grid = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]


def left_connected(i, j, grid):
    if j > 0:
        if grid[i][j - 1] == 1:
            return True
        else:
            return False


def right_connected(i, j, grid, cols):
    if j < cols - 1:
        if grid[i][j + 1] == 1:
            return True
        else:
            return False


def up_connected(i, j, grid, rows):
    if 0 < i:
        if grid[i - 1][j] == 1:
            return True
        else:
            return False


def down_connected(i, j, grid, rows):
    if i < rows - 1:
        if grid[i + 1][j] == 1:
            return True
        else:
            return False


rows = len(grid)
cols = len(grid[0])
p = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 0:
            continue
        else:
            edges = 4
            if left_connected(i, j, grid):
                edges -= 1
            if right_connected(i, j, grid, cols):
                edges -= 1
            if up_connected(i, j, grid, rows):
                edges -= 1
            if down_connected(i, j, grid, rows):
                edges -= 1
        p = p + edges

print(p)
