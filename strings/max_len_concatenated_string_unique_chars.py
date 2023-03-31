# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

arr = ["cha", "r", "act", "ers"]


def max_len_str_unique_chars(words):
    unique_strs = ['', ]
    max_len = 0

    def valid(s):
        return len(s) == len(set(s))

    for word in words:
        for s in unique_strs:
            if valid(word + s):
                unique_strs.append(word + s)
                max_len = max(max_len, len(word) + len(s))
    return max_len


print(max_len_str_unique_chars(arr))