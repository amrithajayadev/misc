import time
from timeit import timeit

nums = [-2, -1, 0, 3, 5, 9, 12]
target = 9


def binary_search(nums, target, l, r):
    if l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            print(f"Found {target} at index {mid}")
            return mid
        if target < nums[mid]:
            return binary_search(nums, target, l, mid-1)
        else:
            return binary_search(nums, target, mid+1, r)
    else:
        print(f"{target} not found")

st = time.time()
binary_search(nums, 12, 0, len(nums) - 1)
et = time.time()
print(et-st)


def binary_search_2(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            print(f"Found {target} at index:{mid}")
            return True
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    print(f"Couldn't find the target num {target}")
    return False


st = time.time()
binary_search_2(nums, 12)
et = time.time()
print(et-st)
