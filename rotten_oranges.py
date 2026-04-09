grid = [[2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]]
from collections import deque


# grid = [[2, 1, 0, 2, 1],
#         [1, 0, 1, 2, 1],
#         [1, 0, 0, 2, 1]]

def bfs1(grid, rows, cols, q, fresh):
    mins = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q and fresh > 0:
        for i in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                R = dr + r
                C = dc + c
                if 0 <= R < rows and 0 <= C < cols and grid[R][C] == 1:
                    q.append((R, C))
                    grid[R][C] = 2
                    fresh -= 1
        mins += 1
    return mins if fresh == 0 else -1


def rotting_oranges_time(grid):
    rows = len(grid)
    cols = len(grid[0])
    mins, fresh = 0, 0
    q = deque()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                q.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1
    mins = bfs1(grid, rows, cols, q, fresh)
    print(mins)


# rotting_oranges_time(grid)

def orangesRotting(grid) -> int:
    """
    BFS v/s DFS
    BFS for shortest path. At each level, shortest path is traversed. Num levels = time
    DFS will explore the path completely
    and may not always be the shortest path. Will need to keep DFSing on each point. not optimal
    """

    R = len(grid)
    C = len(grid[0])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 2:
                q.append((i, j))
    time = 0
    while q:
        r, c = q.popleft()
        for i, j in dirs:
            nr = r + i
            nc = c + j
            if 0 <= nr < R and 0 <= nc < R and grid[nr][nc] == 1:
                q.append((nr, nc))
                grid[nr][nc] = 2
        time += 1
    return time
grid = [[1,1,0],[0,1,1],[0,1,2]]
print(orangesRotting(grid))