# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/
def dfs(i, j, R, C, grid):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    count = 0
    for x, y in dirs:
        r = i + x
        c = j + y
        if 0 <= r < R and 0 <= c < C and grid[r][c] == 1:
            grid[r][c] = 0
            count += 1
            dfs(r, c, R, C, grid)
    return count


def dfs1(i, j, R, C, grid, visited):
    if (i >= R or i < 0) or (j >= C or j < 0) or visited[i][j] or grid[i][j] ==0:
        return
    visited[i][j] = True
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for x, y in dirs:
        r = i + x
        c = j + y
        dfs1(r, c, R, C, grid, visited)


def count_islands(grid):
    R = len(grid)
    C = len(grid[0])
    count = 0
    visited = [[False] * C] * R
    for i in range(R):
        for j in range(C):
            if not visited[i][j] and grid[i][j] == 1:
                dfs1(i, j, R, C, grid, visited)
                count += 1
    return count


def min_days_to_disconnect(grid):
    R = len(grid)
    C = len(grid[0])
    days = 0

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                days += dfs(i, j, R, C, grid)
    return days


# grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
grid = [[1, 0, 1], [0, 1, 1], [1, 1, 1]]
# grid = [[1, 1]]
# print(min_days_to_disconnect(grid))
print(count_islands(grid))