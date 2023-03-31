# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

def shortest_continuous_subarray_len(arr):
    n = len(arr)
    end = 0
    start = n

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                start = min(i, start)
                end = max(j, end)

    # print(start, end)
    return end - start + 1 if end > start else 0


print(shortest_continuous_subarray_len([2, 6, 4, 8, 10, 9, 15]))

def shortest_continuous_sbarray_opt(arr):
    min_from_end = []
    max_from_beginning = []
    n = len(arr)
    for i in range(n):
        if not max_from_beginning:
            max_from_beginning.append(arr[i])
        else:
            max_from_beginning.append(max(arr[i], max_from_beginning[-1]))
    for i in range(n-1, -1, -1):
        if not min_from_end:
            min_from_end.append(arr[i])
        else:
            min_from_end.append(min(arr[i], min_from_end[-1]))
    min_from_end = min_from_end[::-1]

    print(min_from_end)
    print(max_from_beginning)
    print(arr)
    start = n
    end = 0
    for i in range(n):
        if arr[i] < max_from_beginning[i]:
            end += 1
    for i in range(n-1, -1, -1):
        if arr[i] > min_from_end[i]:
            start -= 1

    print(start, end)
    return end-start+1

print(shortest_continuous_sbarray_opt([2, 3, 9 , 7, 6 , 4, 5, 12, 15]))


def shortest_unsorted_subarray_3(nums):
    i = 0
    j = len(nums)-1

    while i < j:
        if nums[i] < nums[j]:
            if nums[i+1] > nums[i]:
                i += 1
            if nums[j-1] < nums[j]:
                j -= 1
        print(i, j)
    print(j-i+1)

# shortest_unsorted_subarray_3([2,6,4,8,10,9,15])