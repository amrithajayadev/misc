from collections import Counter


def min_window_substring(s, t):
    if len(s) < len(t):
        return ""
    freq_map_t = Counter(t)
    required = len(freq_map_t)
    formed = 0
    min_len = float('inf')
    i = 0
    j = 0
    n = len(s)
    start = 0
    end = 0
    curr_map = {}
    while j < n:
        if s[j] in curr_map:
            curr_map[s[j]] += 1
        else:
            curr_map[s[j]] = 1
        if s[j] in freq_map_t and curr_map[s[j]] == freq_map_t[s[j]]:
            formed += 1
            print(formed)
        while i <= j and formed == required:
            print(s[i:j+1])
            if j-i+1 < min_len:
                min_len = j-i+1
                start = i
                end = j
            print(i, j, min_len)
            curr_map[s[i]] -= 1
            if s[i] in freq_map_t and curr_map[s[i]] < freq_map_t[s[i]]:
                formed -= 1
            i += 1
        j += 1
    print(min_len)
    return s[start:end+1]

#
# s = "ADOBECODEBANC"
# t = "ABC"

s = "AA"
t = "AA"
min_window_substring(s, t)