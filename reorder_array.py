from collections import Counter


def canReorderDoubled(arr):
    """
    :type arr: List[int]
    :rtype: bool
    Iterate through the nums.
    Check if half of numbers have it's double or half present

    sort on absolute value.
    iterate till middle and check if all have it's double present in the arr.

    """
    arr.sort()
    freq_map = Counter(arr)
    i = 0
    while i < len(arr):
        if freq_map[arr[i]] <= 0:
            i += 1
            continue
        if arr[i] * 2 in freq_map and freq_map[2 * arr[i]] > 0:
            freq_map[2 * arr[i]] -= 1
            freq_map[arr[i]] -= 1
        elif arr[i] % 2 == 0 and arr[i] // 2 in freq_map and freq_map[arr[i] // 2] > 0:
            freq_map[arr[i] // 2] -= 1
            freq_map[arr[i]] -= 1
        i += 1
    print(freq_map)
    for k, v in freq_map.items():
        if v != 0:
            return False

    return True


# arr = [4,-2,2,-4]
# arr = [3, 1, 3, 6]
# arr = [4,-2,2,-4,-4,-4]
# arr = [1,1,3, 3, 6,12]
arr = [2,4,0,0,8,1]
print(canReorderDoubled(arr))
