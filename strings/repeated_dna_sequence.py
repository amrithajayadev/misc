# s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# s = "AAAAAAAAAAAAA"
from collections import Counter

s = "AAAAAAAAAAA"
def get_repeated_sequences(s):
    i = 0
    j = i + 9
    n = len(s)
    dna_map = {}
    while j < n:
        if s[i:j+1] in dna_map:
            dna_map[s[i:j+1]] += 1
        else:
            dna_map[s[i:j+1]] = 1
        i += 1
        j += 1
    print(dna_map)
    patters = []
    for p, v in dna_map.items():
        if v > 1:
            patters.append(p)
    return patters


print(get_repeated_sequences(s))

num_map = Counter([7,5,7,1])