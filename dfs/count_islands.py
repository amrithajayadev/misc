def dfs(grid, i, j, R, C, visited):
    if 0 > i or 0 > j or i >= R or j >= C or grid[i][j] != 1 or visited[i][j] == True:
        return
    visited[i][j] = True
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in dirs:
        r = i + dr
        c = j + dc
        dfs(grid, r, c, R, C, visited)


def count_islands(grid, R, C, visited):
    count = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1 and visited[i][j] == False:
                dfs(grid, i, j, R, C, visited)
                count += 1
    return count


def numOfIslands(rows: int, cols: int, operators):
    # code here
    sol = []
    grid = [[0] * cols for _ in range(rows)]

    for r, c in operators:
        visited = [[False] * cols for _ in range(rows)]
        grid[r][c] = 1
        sol.append(count_islands(grid, rows, cols, visited))
        for i in range(rows):
            print(grid[i])
        print("\n")
    return sol


operators = [[1, 1], [0, 1], [3, 3], [3, 4]]
print(numOfIslands(4, 5, operators))