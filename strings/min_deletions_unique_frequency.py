from collections import Counter


def minDeletions(s: str) -> int:
    freq_map = Counter(s)
    unique_chars = sorted(freq_map, key=freq_map.get, reverse=True)
    count = 0
    for i in range(len(unique_chars) - 1):
        if freq_map[unique_chars[i]] == freq_map[unique_chars[i + 1]]:
            freq_map[unique_chars[i + 1]] -= 1
            count += 1
            if freq_map[unique_chars[i + 1]] == 0:
                freq_map.pop(unique_chars[i + 1])
                unique_chars.pop(i + 1)

    return count


# print(minDeletions("ceabaacb"))
# print(minDeletions("aab"))
# print(minDeletions("aaabbbcc"))
# print(minDeletions("abcabc"))

def min_deletions(s):
    count = 0
    freq_map = Counter(s)
    already_covered_frequencies = set()

    for ch, freq in freq_map.items():
        while freq > 0 and freq in already_covered_frequencies:
            freq -= 1
            count += 1
        already_covered_frequencies.add(freq)
    return count

print(min_deletions("ceabaacb"))
print(min_deletions("aab"))
print(min_deletions("aaabbbcc"))
print(min_deletions("abcabc"))