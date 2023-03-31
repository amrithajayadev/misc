# arr = [4, 1, 1, 1, 2, 3, 5]
# n = len(arr)
# k = 5


def largest_subarray_of_sum_k(arr, k, n):
    i = 0
    j = 0
    sum = 0
    max_len = 0
    sub_array = []
    while j < n and i < n:
        sum += arr[j]
        print(sum)
        while sum > k:
            sum -= arr[i]
            i += 1
        if sum == k:
            max_len = max(max_len, j - i + 1)
            sub_array.append((i, j))
            sum -= arr[i]
            i += 1
        j += 1
    print(max_len)
    # print(sub_array)
    for i, j in sub_array:
        print(arr[i:j + 1])


arr = [-5, 8, -14, 2, 4, 12]
k = -5
n = len(arr)
largest_subarray_of_sum_k(arr, k, n)

def largest_subarray_of_sum_k_neg(arr, k, n):
    j = 0
    i = 0
    max_len = 0
    sum = 0
    while j <n and i <n:
        sum += arr[j]
        if sum == k:
            max_len = max(max_len, j-i+1)
        else:
            sum + arr[j+1]
            sum + arr[j+1] - arr[i]

