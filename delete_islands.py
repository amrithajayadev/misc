def print1(grid):
    for item in grid:
        print(item)


def delete_islands(grid):
    # 1 -> land
    # 0 -> water
    r = len(grid)
    c = len(grid[0])
    change = []
    for i in range(1, r - 1):
        for j in range(1, c - 1):
            if grid[i - 1][j] == grid[i][j - 1] == grid[i][j + 1] == grid[i + 1][j] == 1 and not \
            (grid[i + 1][j + 1] == 0 or grid[i + 1][j - 1] == 0 or grid[i - 1][j - 1] == 0 or grid[i - 1][j + 1] == 0):
                change.append((i, j))

    for item in change:
        i, j = item
        grid[i][j] = 0
    print1(grid)


inp1 = [[0, 0, 0, 1, 1, 1],
       [0, 0, 0, 1, 1, 1],
       [1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1, 1]] #works

inp2 = [[1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1]] # works

inp = [[1, 1, 1, 0, 1, 1, 1],
 [1, 1, 1, 0, 1, 1, 1],
 [1, 1, 1, 0, 1, 1, 1],
 [0, 0, 0, 0, 1, 1, 1],
 [1, 1, 1, 0, 1, 1, 1]]
delete_islands(inp)
