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


grid = [[1, 0, 1], [0, 1, 1], [1, 1, 1]]


# print(find_number_of_islands(grid))


# start iterating from the first cell.
# If first cell is 1, then increment the island_count by 1.
# Mark the cell as visited
# Check the adjacent cells left, right, up and down.
# If any of them is 1, continue to check the adjacent cells of new cell
# If 0, skip the check
# process the next cell if not already visited.

def count_islands(grid):
    R = len(grid)
    C = len(grid[0])
    visited = set()
    island_count = 0

    def dfs(i, j):
        # check the edge case first
        # check if visited again because dfs called again from here.
        if i >= R or j >= C or i < 0 or j < 0 or (i, j) in visited:
            return

        # mark the cell visited
        visited.add((i, j))
        # recursively dfs on the current cell's adjacent cells if 1
        if grid[i][j] == "1":
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

    # Cover all cells one by one.
    # But only unvisited and "1" cells need to be processed.
    # Once we exit a dfs, we would have found an island and marked
    # it's adjacent cells as visited so that it is not processed again
    for i in range(R):
        for j in range(C):
            if grid[i][j] == "1" and (i, j) not in visited:
                dfs(i, j)
                island_count += 1
    # print(visited)
    # print(len(visited))
    return island_count


print(count_islands(grid))
print(count_islands(
    grid=[["0", "0", "1", "1", "0"],
          ["1", "1", "1", "1", "0"],
          ["0", "1", "0", "0", "0"],
          ["0", "0", "0", "0", "0"]]))

print(count_islands(
    grid=[["1", "0", "1", "1", "1"],
          ["0", "0", "1", "1", "0"],
          ["0", "1", "0", "0", "0"],
          ["0", "0", "0", "1", "1"]]))
