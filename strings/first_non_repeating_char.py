# https://leetcode.com/problems/first-unique-character-in-a-string/
from collections import Counter

s = "leetcode"


def find_first_non_repeating_char(s):
    d = Counter(s)
    for idx, char in enumerate(s):
        if d[char] == 1:
            return idx
    return -1
print(find_first_non_repeating_char(s))
print(find_first_non_repeating_char("loveleetcode"))
print(find_first_non_repeating_char("aabb"))