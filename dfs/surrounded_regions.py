# https://leetcode.com/problems/surrounded-regions/
# board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
board = [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]

def dfs(board, i, j, r, c):
    if i < 0 or j < 0 or j >= c or i >= r or board[i][j] != 'O':
        return
    board[i][j] = 'T'
    adjacent = [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]
    for x, y in adjacent:
        dfs(board, x, y, r, c)


def solve(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    r = len(board)
    c = len(board[0])

    # check borders

    # check all elements along extreme columns
    for i in range(r):
        dfs(board, i, 0, r, c)
        dfs(board, i, c - 1, r, c)

    # check all elements along extreme rows
    for i in range(c):
        dfs(board, 0, i, r, c)
        dfs(board, r-1, i, r, c)

    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'T':
                board[i][j] = 'O'

    print(board)

solve(board)