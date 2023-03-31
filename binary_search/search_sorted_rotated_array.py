def binary_search_for_pivot2(nums):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if mid == start:
            return mid
        elif nums[mid] < nums[start]:
            end = mid - 1
        elif nums[mid] > nums[end]:
            start = mid
        else:
            return -1


def binary_search(nums, start, end, target):
    if start <= end:
        mid = (start + end) // 2
        print(f"start={start}, end={end}, mid= {mid}")
        if nums[mid] == target:
            print(f"from == condition start={start}, end={end}, mid= {mid}")
            return mid
        if target < nums[mid]:
            end = mid - 1
            return binary_search(nums, start, end, target)
        else:
            start = mid + 1
            return binary_search(nums, start, end, target)
    else:
        return -1


def search_rotated_array(a, target):
    pivot = binary_search_for_pivot2(a)
    print(f"pivot : {pivot}")
    answer_left = binary_search(a, 0, pivot + 1, target)
    answer_right = binary_search(a, pivot + 1, len(a) - 1, target)

    if answer_right != -1:
        print(answer_right)
    elif answer_left != -1:
        print(answer_left)
    else:
        print(-1)


# search_rotated_array([12, 13, 100, 1, 2, 3, 6, 7, 8, 9, 10], 7)
# search_rotated_array([6, 7, 8, 9, 10, 1, 2, 3, 5], 10)
# print(binary_search([12, 13, 100, 1, 2, 3, 6, 7, 8, 9, 10], 3, 10, 12))
# a = [6, 7, 8, 9, 10, 1, 2, 3, 5] # works ans 4
# a = [12, 13, 100, 1, 2, 3, 6, 7, 8, 9, 10] # ans 2
a = [1, 2, 3]  # returns -1
# print(binary_search_for_pivot2(a))
search_rotated_array(a, 3)
