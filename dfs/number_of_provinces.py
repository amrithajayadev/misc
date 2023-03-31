# https://leetcode.com/problems/number-of-provinces/
# isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
isConnected = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]


def dfs(i, j, r, c, isConnected, visited):
    if i < 0 or j < 0 or i >= r or j >= c or isConnected[i][j] != 1:
        return
    isConnected[i][j] = 1
    visited.append((i, j))
    adjacent = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
    for x, y in adjacent:
        if (x, y) not in visited:
            dfs(x, y, r, c, isConnected, visited)


def find_number_of_provinces(isConnected):
    r = len(isConnected)
    c = len(isConnected[0])
    count = 0
    visited = []
    for i in range(r):
        for j in range(c):
            if (i, j) not in visited:
                dfs(i, j, r, c, isConnected, visited)
                visited.append((i, j))
                count += 1
    print(isConnected)
    print(visited)
    print(count)


find_number_of_provinces(isConnected)