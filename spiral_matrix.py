matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]] # works

# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


def print_spiral_matrix(matrix):
    R = len(matrix)
    C = len(matrix[0])
    arr = []
    c = 0
    r = 0

    while r < R and c < C:
        # move right
        for j in range(c, C):
            arr.append(matrix[r][j])
        r += 1

        # move down
        for i in range(r, R):
            arr.append(matrix[i][C - 1])
        C -= 1

        # move left
        if r < R:
            for j in range(C - 1, c - 1, -1):
                arr.append(matrix[R - 1][j])
            R -= 1

        # move up
        if c < C:
            for i in range(R - 1, r - 1, -1):
                arr.append(matrix[i][c])
            c += 1
        print(arr)
    print(arr)


print_spiral_matrix(matrix)