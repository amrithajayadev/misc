# https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/

def count_all_paths(i, j, R, C, count):
    if i > R - 1 or j > C - 1:
        return 0
    if i == R - 1 and j == C - 1:
        return 1
    count += count_all_paths(i, j + 1, R, C, count) + count_all_paths(i + 1, j, R, C, count)
    return count


# print(count_all_paths(0, 0, 2, 2, 0))
# print(count_all_paths(0, 0, 2, 3, 0))
# print(count_all_paths(0, 0, 23, 12, 0))
# print(count_all_paths(0, 0, 3, 7, 0))

# bottom up approach (building from scratch)
def count_unique_paths_dp(r, c, t):
    t[0][0] = 1
    for i in range(c + 1):
        t[0][i] = 1
    for j in range(r + 1):
        t[j][0] = 1

    for i in range(1, r + 1):
        for j in range(1, c + 1):
            t[i][j] = t[i - 1][j] + t[i][j - 1]
    return t[r][c]


# C = 12
# R = 23

# R = 3
# C = 7
# t = [[0] * C] * R
# print(count_unique_paths_dp(R - 1, C - 1, t))

obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

# https://leetcode.com/problems/unique-paths-ii/
def count_unique_paths_obstacles(obstacleGrid, r, c, t):
    t[0][0] = 1
    for i in range(c + 1):
        t[0][i] = 1 if obstacleGrid[r][c] == 0 else 0
    for j in range(r + 1):
        t[j][0] = 1 if obstacleGrid[r][c] == 0 else 0

    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if obstacleGrid[i][j] == 0:
                t[i][j] = t[i - 1][j] + t[i][j - 1]
            else:
                t[i][j] = 0
    return t[r][c]


R = len(obstacleGrid)
C = len(obstacleGrid[0])
t = [[0] * C] * R
print(count_unique_paths_obstacles(obstacleGrid, R-1, C-1, t))