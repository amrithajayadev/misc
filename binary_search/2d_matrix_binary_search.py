def searchMatrix(matrix, target) -> bool:
    start = 0
    end = len(matrix)
    while start < end:
        mid = (start + end) // 2
        if target < matrix[mid][0]:
            end = mid
        elif mid < end - 1 and target >= matrix[mid + 1][0]:
            start = mid + 1
        else:
            return binary_search(matrix[mid], target)


def binary_search(arr, target):
    s = 0
    e = len(arr)
    while s < e:
        mid = (s + e) // 2
        if target < arr[mid]:
            e = mid
        elif target > arr[mid]:
            s = mid + 1
        else:
            return True
    return False


# matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# target = 22
matrix = [[1], [3], [5]]
target = 5
if searchMatrix(matrix, target):
    print("found")
else:
    print("not found")