# https://leetcode.com/problems/rotate-image/
# pick one element from each list and put them in one list, repeat for all lists.
from collections import Counter

matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
rotated = [[] for _ in range(len(matrix))]
for i in range(len(matrix)-1, -1, -1):
    for j in range(len(matrix)):
        if len(rotated[j]) == 0:
            rotated[j] = [matrix[i][j]]
        else:
            rotated[j].append(matrix[i][j])
print(rotated)
Counter("abccccdd")