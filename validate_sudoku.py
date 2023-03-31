from collections import Counter

s = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]

def validate(s):
    n = len(s)
    m = len(s[0])
    i = 0
    j = 0
    while i < n and j < m:
        vertical_elems = []
        horizontal = Counter(s[i])
        horizontal.pop('.')
        if len(horizontal) != sum(horizontal.values()):
            return False
        for k in range(n):
            vertical_elems.append(s[k][i])
        vertical = Counter(vertical_elems)
        if len(vertical) != sum(vertical.values()):
            return False
        square = s[i][j:j+3] + s[i+1][j:j+3] + s[i+2][j+3]