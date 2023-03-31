str1 = "xfforaxbforfxfrofr"
str2 = "for"


def is_anagram(str1, i, j, str2):
    for idx in range(i, j + 1):
        if str1[idx] not in str2:
            return False
    return True


def count_occurrences_of_anagram(str1, str2):
    k = len(str2)
    n = len(str1)
    i = 0
    j = i + k - 1
    count = 0
    while j < n:
        if is_anagram(str1, i, j, str2):
            count += 1
        i += 1
        j += 1
    return count


print(count_occurrences_of_anagram(str1, str2))


def count_occurrences_of_anagram_optimized(str1, str2):
    k = len(str2)
    n = len(str1)
    i = 0
    j = 0
    count = 0
    char_freq = {}
    for c in str2:
        if c in char_freq:
            char_freq[c] += 1
        else:
            char_freq[c] = 1

    # could have done this in the loop, but overhead of traversing and summing the map values
    total_char_frequency = sum(char_freq.values())

    while j < n:
        if str1[j] in char_freq:  # calculation
            total_char_frequency -= 1
        if j - i + 1 < k:  # till window size is not reached, increment j
            j += 1
        elif j - i + 1 == k:
            if total_char_frequency == 0:  # use calc
                count += 1
            if str1[i] in char_freq:  # before incrementing i, reverse the calculation done for str2[i]
                total_char_frequency += 1
            i += 1
            j += 1
    return count


print(count_occurrences_of_anagram_optimized(str1, str2))
