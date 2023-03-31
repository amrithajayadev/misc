# https://leetcode.com/problems/palindrome-pairs/
def check_palindrome(word):
    i = 0
    j = len(word) - 1
    while i <= j:
        if word[i] != word[j]:
            return False
        else:
            i += 1
            j -= 1
    return True

def find_palindrome_pairs(words):
    n = len(words)
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if check_palindrome(words[i] + words[j]):
                pairs.append([i, j])
            if check_palindrome(words[j] + words[i]):
                pairs.append([j, i])

    return pairs


# words = ["abcd", "dcba", "lls", "s", "sssll"]
# words = ["bat","tab","cat"]
words = ["a",""]
print(find_palindrome_pairs(words))