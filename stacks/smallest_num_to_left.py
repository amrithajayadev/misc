def smallest_num_to_left(nums):
    stack = [0]
    for i in range(1, len(nums)):
        if stack and nums[stack[-1]] > nums[i]:
            stack.append(i)
    # print(stack)
    res = []
    for i in range(len(stack)):
        sell_day = stack[i + 1] - 1 if i < len(stack) - 1 else len(nums) - 1
        if stack[i] != sell_day:
            res.append([stack[i], sell_day])
    return res


# smallest_num_to_left([100,180, 260, 310, 40, 535, 695])
# smallest_num_to_left([4,2,2,2,4])
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def smallest_num_to_left(nums):
    profit = []
    min_so_far = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < min_so_far:
            min_so_far = nums[i]
        profit.append(nums[i] - min_so_far)
    print(max(profit))


# smallest_num_to_left([7, 1, 5, 3, 6, 4])


# https://leetcode.com/problems/two-furthest-houses-with-different-colors/

def max_dist(l, r, nums):
    if l > r:
        return -1
    if nums[l] != nums[r]:
        return r - l
    return max(max_dist(l + 1, r, nums), max_dist(l, r - 1, nums))


# colors = [1, 1, 1, 6, 1, 1, 1]
# print(max_dist(0, len(colors) - 1, colors))

# colors = [0,1]
colors = [6, 6, 6, 6, 6, 6, 6, 6, 6, 19, 19, 6, 6]


# print(max_dist(0, len(colors) - 1, colors))

def max_dist_memoized(l, r, nums, t):
    if l > r:
        return -1
    if t[l][r] != -1:
        return t[l][r]
    elif nums[l] != nums[r]:
        t[l][r] = r - l
    return max(max_dist_memoized(l + 1, r, nums, t), max_dist_memoized(l, r - 1, nums, t))


t = [[-1] * len(colors)] * len(colors)
print(max_dist_memoized(0, len(colors) - 1, colors, t))
print(t)