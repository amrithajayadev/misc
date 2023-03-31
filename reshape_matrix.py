# https://leetcode.com/problems/reshape-the-matrix/

def reshape_matrix(mat, r, c):
    m = len(mat)
    n = len(mat[0])
    reshaped = []
    if m * n != r * c:
        return mat
    if m == r and n == c:
        return mat
    flattened = []
    for i in range(m):
        flattened.extend(mat[i])
    print(flattened)
    for i in range(0, r * c, c):
        reshaped.append(flattened[i:c+i])
    print(reshaped)


# mat = [[1, 2,3,4,5,6], [3, 4,5,6,7,8]]
# r = 3
# c = 4

mat = [[1,2], [3,4]]
r = 1
c = 4
reshape_matrix(mat, r, c)