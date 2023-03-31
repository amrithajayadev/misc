# https://leetcode.com/problems/word-search-ii/

def word_search_2(grid, words):
    R = len(grid)
    C = len(grid[0])
    found_list = []
    for word in words:
        print(f"finding {word}")
        found = ""
        i = 0
        j = 0
        k = 0
        while 0 <= i < R and 0 <= j < C and k < len(word):
            if grid[i][j] == word[k]:
                found += word[k]
            elif grid[i + 1][j] == word[k]:
                i += 1
                found += word[k]
            elif grid[i][j + 1] == word[k]:
                j += 1
                found += word[k]
            # elif grid[i - 1][j] == word[k]:
            #     i -= 1
            #     found += word[k]
            # elif grid[i][j - 1] == word[k]:
            #     j -= 1
            #     found += word[k]
            k += 1
        print(found)
        if found in words:
            found_list.append(found)
    print(found_list)


# board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "e", "a", "t"]]
# words = ["oath", "pea", "eat", "rain"]


# word_search(board, words)

def word_search(grid, word):
    found = False
    visited = []
    visited_set = set()
    R = len(grid)
    C = len(grid[0])

    def dfs(i, j, k, visited, visited_set, found):
        if i < 0 or i >= R or j < 0 or j >= C or word[k] != grid[i][j] or (i, j) in visited_set or not found:
            return

        if k == len(word):
            return True
        visited += [(i, j)]
        visited_set.add((i, j))
        dirs = [(0, 1), (-1, 0), (1, 0), (0, -1)]
        for r, c in dirs:
            X = i + r
            Y = j + c
            dfs(X, Y, k + 1, visited, visited_set, found)
        if not found:
            visited_set.remove(visited.pop())

    for i in range(R):
        for j in range(C):
            return dfs(i, j, 0, visited, visited_set, found)
    return False


# if word_search(board, "oath"):
#     print("true")
# else:
#     print("false")


def word_search_1(board, word):
    R = len(board)
    C = len(board[0])

    def dfs(i, r, c):
        if i == len(word):
            return True

        if 0 <= r < R and 0 <= c < C and board[r][c] == word[i]:
            board[r][c] = '#'
            d1 = dfs(i + 1, r + 1, c)
            d2 = dfs(i + 1, r - 1, c)
            d3 = dfs(i + 1, r, c + 1)
            d4 = dfs(i + 1, r, c - 1)
            board[r][c] = word[i]
            return any([d1, d2, d3, d4])
        return False

    for j in range(R):
        for k in range(C):
            if board[j][k] == word[0] and dfs(0, j, k):
                return True
    return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABFD"
if word_search_1(board, word):
    print(True)
else:
    print(False)