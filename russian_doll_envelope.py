envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]


def merge_sorted_arrays(left, right, m, n):
    sorted_array = []
    i = 0
    j = 0
    while i < m and j < n:
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    if i < m:
        sorted_array.extend(left[i:])
    if j < n:
        sorted_array.extend(right[j:])
    return sorted_array


def merge_sort(envelopes, sorted_array):
    if len(envelopes) > 1:
        mid = len(envelopes) // 2
        left = merge_sort(envelopes[:mid], sorted_list)
        right = merge_sort(envelopes[mid:], sorted_list)

        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
        if i < len(left):
            sorted_array.extend(left[i:])
        if j < len(right):
            sorted_array.extend(right[j:])
        return sorted_array


def sort_envelopes(envelopes):
    sorted_envelopes = []


# left = [1, 5, 7, 13, 15]
# right = [2, 4, 10]
# merge_sorted_arrays(left, right, len(left), len(right))

arr = [1, 13, 14, 2, 6, 5, 9, 10, 2]
sorted_list = []
e = merge_sort(arr, sorted_list)
print(e)
