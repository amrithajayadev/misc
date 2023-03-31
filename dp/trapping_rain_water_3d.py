# https://leetcode.com/problems/trapping-rain-water-ii/submissions/
def trapRainWater(heightMap) -> int:
    # find greatest element on left and right of the middle blocks.
    # compare with the blocks to north and south of it and min of it is the
    # unit amount of water that can be held.

    left = []
    n = len(heightMap[1])
    for i in range(0, n):
        if not left:
            left.append(heightMap[1][i])
        else:
            left.append(max(left[i - 1], heightMap[1][i]))

    right = []
    for i in range(n - 1, -1, -1):
        if not right:
            right.append(heightMap[1][i])
        else:
            right.append(max(right[-1], heightMap[1][i]))
    right = right[::-1]

    cols = len(heightMap)
    north = []
    for i in range(0, cols):
        for j in range(0, n):
            if not north:
                north.append(heightMap[j][i])
            else:
                north.append(max(north[-1], heightMap[j][i]))

    south = []
    for i in range(cols - 1, -1, -1):
        for j in range(n, -1, -1):
            if not south:
                south.append(heightMap[j][i])
            else:
                south.append(max(south[-1], heightMap[j][i]))
    south = south[::-1]

    water = 0
    for i in range(0, n):
        water += max(min(left[i], right[i], north[i], south[i]) - heightMap[1][i], 0)

    return water