# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

def is_palindrome(word):
    return word == word[::-1]


def longest_palindrome(words):
    palindromes = []
    for word in words:
        if is_palindrome(word):
            palindromes.append(word)
        elif word[::-1] in words:
            palindromes.append(word + word[::-1])
    for word in words:
        for pal in palindromes:
            if word not in pal and word[::-1] in words and not is_palindrome(word):
                palindromes.append(word+pal+word[::-1])
    print(palindromes)


# words = ["ab", "ty", "yt", "lc", "cl", "ab"]
# words = ["lc","cl","gg"]
words = ["cc","ll","xx"]
longest_palindrome(words)