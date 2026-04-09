from collections import deque


def islandsAndTreasure(grid) -> None:
    R = len(grid)
    C = len(grid[0])

    def dfs(r, c, R, C, visited, val):
        if r < 0 or c < 0 or r >= R or c >= C or (r, c) in visited or grid[r][c] == -1:
            return

        visited.add((r, c))
        print(f"Before, grid[{r}][{c}] :{grid[r][c]}")
        grid[r][c] = min(grid[r][c], val)
        print(f"After changing to val={val}, grid[{r}][{c}] :{grid[r][c]}")
        dfs(r - 1, c, R, C, visited, val + 1)
        dfs(r + 1, c, R, C, visited, val + 1)
        dfs(r, c - 1, R, C, visited, val + 1)
        dfs(r, c + 1, R, C, visited, val + 1)
        return

    for i in range(R):
        for j in range(C):
            visited = set()
            if grid[i][j] == 0 and (i, j) not in visited:
                print(f"Visiting ({i},{j})")
                dfs(i, j, R, C, visited, 0)

    print(grid)


# grid = [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]
grid = [[2147483647, 2147483647, 2147483647], [2147483647, -1, 2147483647], [0, 2147483647, 2147483647]]

# print(islandsAndTreasure(grid))


def islandsAndTreasureBfs(grid):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    R = len(grid)
    C = len(grid[0])

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 0:
                q.append((i, j))

    while q:
        r, c = q.popleft()
        for i, j in directions:
            nr = r + i
            nc = c + j
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 2147483647:
                q.append((nr, nc))
                grid[nr][nc] = grid[r][c] + 1

    print(grid)

islandsAndTreasureBfs(grid)

