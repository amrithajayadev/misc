arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3


# o/p = [3,3,5,5,6,7]


def max_of_each_subarray(arr, k):
    i = 0
    j = 0
    n = len(arr)
    max_array = []
    output = []
    while j < n:
        if not max_array:
            max_array.append(arr[j])
        else:
            while max_array and max_array[-1] < arr[j]:
                max_array.pop()
            max_array.append(arr[j])

        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            output.append(max_array[0])
            if max_array and max_array[0] == arr[i]:
                max_array.pop(0)
            i += 1
            j += 1
    return output


# print(max_of_each_subarray(arr, 3))

def max_of_each_subarray_my(arr, k):
    i = 0
    j = 1
    n = len(arr)
    max_array = []
    max0 = arr[0]
    output = []
    while j < n:
        max0 = max(max0, arr[j])
        max_array.append(max0)
        if j - i + 2 < k:
            j += 1
        elif j - i + 2 == k:
            if i != 0:
                output.append(max_array[0])
            if max_array:
                max_array.pop(0)
            i += 1
            j += 1
    return output


print(max_of_each_subarray_my(arr, 3))
