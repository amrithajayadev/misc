# https://leetcode.com/problems/word-pattern/
from collections import Counter


def check_pattern_matches(pattern, s):
    p_map = Counter(pattern)
    s_map = Counter(s.split())

    if sum(p_map.values()) != sum(s_map.values()):
        return False
    for pv, sv in zip(p_map.values(), s_map.values()):
        if pv != sv:
            return False
    pattern_word_map = {}
    for pk, sk in zip(p_map.keys(), s_map.keys()):
        pattern_word_map[pk] = sk

    s_list = s.split()
    for i, p in enumerate(pattern):
        if pattern_word_map[p] != s_list[i]:
            return False
    return True


pattern="abba"
s="dog cat cat dog"

# pattern = "abba"
# s = "dog cat cat fish"

# pattern = "aaaa"
# s = "dog cat cat dog"

# pattern = "abab"
# s = "dog cat cat dog"
if check_pattern_matches(pattern, s):
    print("True")
else:
    print("False")