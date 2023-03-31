def check_palindrome(s, i, j):
    if i == j:
        return True
    if s[i] != s[j]:
        return False
    if i < j:
        return check_palindrome(s, i + 1, j - 1)
    return True


def get_longest_palindromic_substring(s):
    start = 0
    end = len(s) - 1
    if start == end:
        return s
    if start < end:
        if check_palindrome(s, start, end):
            return s[start:end]
        elif get_longest_palindromic_substring(s[start + 1:end]):
            start = start + 1
        elif get_longest_palindromic_substring(s[start:end - 1]):
            end = end - 1
    return s[start:end]


print(get_longest_palindromic_substring("bb"))