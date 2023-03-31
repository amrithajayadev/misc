# swap row 0 with col n
# in the sub matrix : r++, c--
# swap row 1 with col n-1
# r++, c--
# swap row 2 with col n-2

def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reflect(matrix):
    n = len(matrix)
    start = 0
    end = n - 1

    while start < end:
        for i in range(n):
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
        start += 1
        end -= 1


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13,14,15,16]]

def rotate(matrix):
    print(matrix)
    transpose(matrix)
    reflect(matrix)
    print(matrix)

rotate(matrix)