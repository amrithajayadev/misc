output = []


def binary_search(nums, start, end, target):
    if start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            end = mid - 1
            return binary_search(nums, start, end, target)
        else:
            start = mid + 1
            return binary_search(nums, start, end, target)
    else:
        return -1


def find_min_max_pos(nums, target):
    target_pos = binary_search(nums, 0, len(nums)-1, target)
    min_pos = max_pos = target_pos
    while min_pos > 0:
        min_pos = min_pos - 1
        if binary_search(nums, 0, min_pos, target) == -1:
            min_pos = min_pos+1
            break
    while max_pos < len(nums):
        max_pos = max_pos + 1
        if binary_search(nums, max_pos, len(nums)-1, target) == -1:
            max_pos = max_pos - 1
            break
    return [min_pos, max_pos]


# print(binary_search(nums, 0, len(nums), 8))
# print(output)
# nums = [5, 7, 7, 8, 8, 8, 10]
# print(find_min_max_pos(nums, 8)) # worked
# print(find_min_max_pos(nums, 5)) # worked
# print(find_min_max_pos(nums, 10)) # worked
# print(find_min_max_pos(nums, 0)) # worked

nums = []
print(find_min_max_pos(nums, 0))