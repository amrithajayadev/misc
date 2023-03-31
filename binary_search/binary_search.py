nums = [-2, -1, 0, 3, 5, 9, 12]
target = 9


def binary_search(nums, target, l, r):
    if l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            print(f"Found {target} at index {mid}")
            return mid

        if target < nums[mid]:
            r = mid - 1
            return binary_search(nums, target, l, r)
        else:
            l = mid + 1
            return binary_search(nums, target, l, r)
    else:
        print(f"{target} not found")


binary_search(nums,-2 , 0, len(nums)-1)
