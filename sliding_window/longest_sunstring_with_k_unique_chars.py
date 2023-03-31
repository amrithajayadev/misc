s = "aabacbebebe"
k = 3
char_freq = {}
max_len = 0
n = len(s)
i = 0
j = 0
while j < n and i < n:
    if s[j] in char_freq:
        char_freq[s[j]] += 1
    else:
        char_freq[s[j]] = 1

    while len(char_freq) > k:
        char_freq[s[i]] -= 1
        if char_freq[s[i]] == 0:
            char_freq.pop(s[i])
        i += 1
    if len(char_freq) == k:
        max_len = max(max_len, j - i + 1)
    j += 1
print(max_len)
