# s = "pwiolkwkewlo"
# i = 0
# j = 0
# n = len(s)
# unique_chars = {}
# max_len = 0
# while j < n:
#     if s[j] not in unique_chars:
#         unique_chars[s[j]] = 1
#     else:
#         unique_chars[s[j]] += 1
#
#     while len(unique_chars) < sum(unique_chars.values()):
#         unique_chars[s[i]] -= 1
#         if unique_chars[s[i]] == 0:
#             unique_chars.pop(s[i])
#         i += 1
#     if len(unique_chars) == sum(unique_chars.values()):
#         max_len = max(max_len, j-i+1)
#     j += 1
#     print(unique_chars)
# print(max_len)

def longest_substring_without_repeating_chars(s):
    i = 0
    j = 0
    st = set()
    max_len = 0
    n = len(s)
    while j < n:
        print(st)
        if s[j] not in st:
            st.add(s[j])
            max_len = max(max_len, len(st))
        else:
            while s[i] in st and i < j:
                st.remove(s[i])
                i += 1
            st.add(s[j])
        j += 1
    return max_len

s = "pwiolkwkewlo"
# s = "xyzyzxx"
s = "abba"
print(longest_substring_without_repeating_chars(s))


