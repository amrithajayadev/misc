from typing import List


def numIslands(grid: List[List[str]]) -> int:
    visited = set()
    R = len(grid)
    C = len(grid[0])

    def bfs(r, c, R, C):
        print("Inside bfs")
        if r >= R or c >= C or r < 0 or c < 0 or (r, c) in visited or grid[r][c] == "0":
            print(f"Not processing (i,j):({i},{j})")
            return False
        visited.add((r, c))
        bfs(r + 1, c, R, C)
        bfs(r - 1, c, R, C)
        bfs(r, c + 1, R, C)
        bfs(r, c - 1, R, C)
        return True

    count = 0
    for i in range(R):
        for j in range(C):
            print(f"current i,j: {i}, {j}")
            if grid[i][j] == "1" and (i, j) not in visited:
                print(f"Processing (i,j):({i},{j})")
                if bfs(i, j, R, C):
                    count += 1
    return count
#
# grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]

grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
print(numIslands(grid))