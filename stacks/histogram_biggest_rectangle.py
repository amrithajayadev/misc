nums = [2, 1, 5, 6, 2, 3, 2]  # works
# nums=[2,2,2,4,4,4]

# nums = [2, 1, 5, 6, 2, 3, 2, 2, 2, 22]
# nums = [1, 1]


def find_left_right_max_index(arr, pos):
    left = right = pos
    l = r = -1
    while left > 0:
        left -= 1
        if arr[left] < arr[pos]:
            l = left + 1
            break
    while right < len(arr) - 1:
        right += 1
        if arr[right] < arr[pos]:
            r = right - 1
            break
    return l, r


def largest_rectangle_bruteforce(nums):
    max_rect = []
    for i in range(0, len(nums)):
        l, r = find_left_right_max_index(nums, i)
        print(f"left={l}, right={r}")
        # left_area = nums[i] * (i - l) if l != -1 else nums[i] * i
        if l == -1:
            left_area = nums[i] * i
        elif l == i:
            left_area = nums[i]
        else:
            left_area = nums[i] * (i - l)
        # right_area = nums[i] * (r - i) if r != -1 else nums[i] * (len(nums) - i)
        if r == -1:
            right_area = nums[i] * (len(nums) - 1 - i)
        elif r == i:
            if r == l:
                right_area = 0
            else:
                right_area = nums[i]
        else:
            right_area = nums[i] * (r - i)
        area = left_area + right_area
        print(f"area={area}")
        max_rect.append(max(area, nums[i]))

    print(max_rect)


def largest_rectange_opt(nums):
    stack = []
    curr_pos = 0
    max_area = 0
    while curr_pos < len(nums):
        if not stack or nums[curr_pos] >= nums[stack[-1]]:
            stack.append(curr_pos)
            curr_pos += 1
        else:
            top_of_stack = stack.pop()
            area = nums[top_of_stack] * ((curr_pos - stack[-1] - 1) if stack else curr_pos)
            max_area = max(max_area, area)
    while stack:
        top_of_stack = stack.pop()
        area = nums[top_of_stack] * ((curr_pos - stack[-1] - 1) if stack else curr_pos)
        max_area = max(max_area, area)
    return max_area


# print(largest_rectange_opt(nums))


def nearest_smaller_left(nums):
    stack = []
    output = []
    n = len(nums)
    for i in range(n):
        if not stack:
            output.append(-1)
        else:
            if nums[stack[-1]] < nums[i]:
                output.append(stack[-1])
            else:
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()
                if stack:
                    output.append(stack[-1])
                else:
                    output.append(-1)
        stack.append(i)
    return output


def nearest_smaller_right(nums):
    stack = []
    output = []
    n = len(nums)
    for i in range(n - 1, -1, -1):
        if not stack:
            output.append(n)
        else:
            if nums[stack[-1]] < nums[i]:
                output.append(stack[-1])
            else:
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()
                if stack:
                    output.append(stack[-1])
                else:
                    output.append(n)
        stack.append(i)
    return output[::-1]


def largest_rectangle_stacks(nums):
    nsl = nearest_smaller_left(nums)
    nsr = nearest_smaller_right(nums)
    # print("nums", nums)
    # print("nsl", nsl)
    # print("nsr", nsr)
    max_area = 0
    n = len(nums)
    for i in range(n):
        width = nsr[i] - nsl[i] - 1
        area = nums[i] * width
        max_area = max(max_area, area)
    print(max_area)


largest_rectangle_stacks(nums)
