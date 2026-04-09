def find_prefix(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    i = 0
    j = 0
    prefix = []
    while i < n1 and j < n2:
        if str1[i] == str2[j]:
            prefix.append(str1[i])
            i += 1
            j += 1
        else:
            break
    return "".join(prefix)


def longestPrefixStringInArray(arr1, arr2):
    arr1.sort()
    arr2.sort()

    str1 = [str(i) for i in arr1]
    str2 = [str(i) for i in arr2]

    n1 = len(str1)
    n2 = len(str2)
    max_prefix = ""
    for i in range(n1 - 1, -1, -1):
        for j in range(n2 - 1, -1, -1):
            curr_prefix = find_prefix(str1[i], str2[j])
            if len(curr_prefix) > len(max_prefix):
                max_prefix = curr_prefix
    return max_prefix


arr1 = [23, 12, 2, 33, 54561, 5, 8932]
arr2 = [14, 8934, 2, 56, 8, 54569]

print(longestPrefixStringInArray(arr1, arr2))
