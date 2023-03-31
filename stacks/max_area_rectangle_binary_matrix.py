from misc.stacks.histogram_biggest_rectangle import nearest_smaller_right, nearest_smaller_left

matrix1 = [[0, 0, 0, 1, 1, 1],
           [0, 0, 0, 1, 1, 1],
           [1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1]]

matrix = [[0, 1, 1, 0],
          [1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 0, 0]]


def mah(arr):
    nsr = nearest_smaller_right(arr)
    nsl = nearest_smaller_left(arr)
    width = []
    area = []
    for r, l in zip(nsr, nsl):
        width.append(r - l - 1)
    for w, l in zip(width, arr):
        area.append(w*l)
    return max(area)


def merge_with_previous_row(n, matrix):
    n_cols = len(matrix[n])
    ret_arr = matrix[n]
    while n > 0:
        for i in range(n_cols):
            if ret_arr[i] != 0:
                ret_arr[i] = ret_arr[i] + matrix[n - 1][i]
        n -= 1
        return ret_arr
    else:
        return matrix[n]


def max_rectangle_in_binary_matrix(matrix):
    n = len(matrix)
    max_area = 0
    for i in range(n):
        nums = merge_with_previous_row(i, matrix)
        print(nums)
        area = mah(nums)
        # print(area)
        max_area = max(max_area, area)
    print(max_area)


max_rectangle_in_binary_matrix(matrix)
