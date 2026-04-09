from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    """
    Iterate through each point in the grid.
    Find the connected points
    return the count of visited points from the dfs
    """
    visited = set()
    R = len(grid)
    C = len(grid[0])
    max_size = 0

    def dfs(r, c, R, C, size):
        if r >= R or c >= C or r < 0 or c < 0 or (r, c) in visited or grid[r][c] == 0:
            return 0
        visited.add((r, c))
        size += 1 + dfs(r - 1, c, R, C, size) + dfs(r + 1, c, R, C, size) + dfs(r, c - 1, R, C, size) + dfs(r, c + 1, R, C, size)
        return size

    for i in range(R):
        for j in range(C):
            curr_size = 0
            if grid[i][j] == 1 and (i, j) not in visited:
                max_size = max(max_size, dfs(i, j, R, C, curr_size))
    return max_size


grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

print(maxAreaOfIsland(grid))
