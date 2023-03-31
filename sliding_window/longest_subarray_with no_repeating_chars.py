s = "pwiolkwkewlo"
i = 0
j = 0
n = len(s)
unique_chars = {}
max_len = 0
while j < n:
    if s[j] not in unique_chars:
        unique_chars[s[j]] = 1
    else:
        unique_chars[s[j]] += 1

    while len(unique_chars) < sum(unique_chars.values()):
        unique_chars[s[i]] -= 1
        if unique_chars[s[i]] == 0:
            unique_chars.pop(s[i])
        i += 1
    if len(unique_chars) == sum(unique_chars.values()):
        max_len = max(max_len, j-i+1)
    j += 1
    print(unique_chars)
print(max_len)
