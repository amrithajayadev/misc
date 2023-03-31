def sort_array_recursive(arr, sorted_array):
    if not arr:
        return sorted_array
    min_num = arr[0]
    min_idx = 0
    for i, n in enumerate(arr):
        if n < min_num:
            min_num = n
            min_idx = i
    sorted_array.append(min_num)
    return sort_array_recursive(arr[:min_idx] + arr[min_idx + 1:], sorted_array)


sorted_arr = []
sort_array_recursive([7, 2, 3, 6, 6, 5, 4, -1], sorted_arr)

print(sorted_arr)


def find_min_in_array(arr, n, min_num, idx):
    if n == 0:
        return min_num, idx
    idx = n
    min_num = min(min_num, find_min_in_array(arr, n-1, min_num, idx))
    return min_num, idx
