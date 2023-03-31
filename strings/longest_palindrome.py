# https://leetcode.com/problems/longest-palindrome/
# https://leetcode.com/problems/longest-palindromic-substring/

from collections import Counter


def find_len_longes_palindrome(s):
    char_freq = Counter(s)
    l = 0
    odd = 0
    for k, v in char_freq.items():
        if v % 2 == 0:
            l += v
        else:
            odd += v % 2
    if odd > 0:
        return len(s) - odd + 1
    else:
        return len(s)


print(find_len_longes_palindrome("abcda"))


def expand_from_char(s, i, j):
    if not s or i > j:
        return

    while i >= 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return i+1, j


def find_longest_palindrome(s):
    longest_subs = ""
    for i in range(len(s)):
        o_i, o_j = expand_from_char(s, i, i)
        e_i, e_j = expand_from_char(s, i, i + 1)

        subs = s[o_i:o_j] if len(s[o_i:o_j]) > len(s[e_i:e_j]) else s[e_i:e_j]
        if len(subs) > len(longest_subs):
            longest_subs = subs
    return longest_subs


# print(find_longest_palindrome("acedcabbacc"))
# print(find_longest_palindrome("racecar"))
# print(find_longest_palindrome("babad"))