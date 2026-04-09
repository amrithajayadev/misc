# [5,6,1,2,3,4]
# [3,4,5,6,1,2]
# [1,2,3,4,5,6]

def find_min_in_rotated_array(arr):
    n = len(arr)
    L = 0
    R = n - 1
    min_v = arr[0]
    while L <= R:
        print(L, R, min_v)
        if arr[L] < arr[R]:
            min_v = min(min_v, arr[L])
            break
        mid = (L + R)//2
        min_v = min(min_v, arr[mid])
        if arr[L] <= arr[mid]:
            L = mid + 1
        else:
            R = mid - 1
    return min_v

# find_min_in_rotated_array([5,6,1,2,3,4])

# find_min_in_rotated_array([3,4,5,6,1,2])

# [1,2,3,4,5,6]
# [5,6,1,2,3,4]
# [3,4,5,6,1,2]

# find 1
def find_in_rotated_sorted_arr(arr, target):
    l = 0
    r = len(arr)-1
    while l <= r:
        mid = (r+l)//2
        if arr[mid] == target:
            return mid
        # left sorted side,
        # if the left is already bigger than the target,
        # if the mid is smaller than the target,
        # then check the right side
        if arr[l] <= arr[mid]:
            if arr[l] > target or arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if arr[mid] > target or arr[r] < target:
                r = mid - 1
            else:
                l = mid + 1
    return -1

print(find_in_rotated_sorted_arr([5,6,1,2,3,4], 1))
print(find_in_rotated_sorted_arr([3,4,5,6,1,2], 1))




