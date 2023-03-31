# grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]
# grid = [[1,0,0,1],
#         [0,1,1,0],
#         [0,1,1,1],
#         [1,0,1,1]]

# 1- land
# 0 - water
def dfs(grid, i, j, r, c):
    if i < 0 or j < 0 or i >= r or j >= c or grid[i][j] != 1:
        return
    grid[i][j] = '.'
    adjacent = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
    for x, y in adjacent:
        dfs(grid, x, y, r, c)


def find_number_of_islands(grid):
    r = len(grid)
    c = len(grid[0])
    land_count = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                dfs(grid, i, j, r, c)
                land_count += 1
    print(grid)

    return land_count

grid = [[1,0,1],[0,1,1], [1,1,1]]
print(find_number_of_islands(grid))