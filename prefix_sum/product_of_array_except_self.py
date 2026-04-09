def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    left_array = [1, 1, 2, 6]
    right_array = [24,12,4,1]

    l_arr = [-1, -1, -1, 0, 0, 0]
    r_arr = [0,0,-9,3,3]
    """

    left_arr = []
    right_arr = []

    left_arr.append(1)
    for i in range(1, len(nums)):
        left_arr.append(nums[i - 1] * left_arr[i - 1])
    print(left_arr)

    right_arr.append(1)
    for i in range(len(nums) - 1, 0, -1):
        right_arr.append(nums[i] * right_arr[len(nums) - i - 1])
    right_arr = right_arr[::-1]
    print(right_arr)

    result = [x * y for x, y in zip(left_arr, right_arr)]
    return result



# Optimize the space usage.
def productExceptSelf_space_optimized(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    nums = [1,2,3,4]
    pre = [1, 1, 2, 6]
    suff = [24,12,4,1]
    o = [24, 12, 8, 6]

    pre = [-1, -1, -1, 0, 0, 0]
    suff = [0,0,-9,3,3]
    o = [0,0,9,0,0]
    """

    prefix_prod = []
    suffix_prod = []
    output = []

    # populate prefix prod -> O(n)
    output.append(1)
    for i in range(0, len(nums)):
        output.append(output[-1] * nums[i])

    # multiply with suffix -> O(n)
    curr = 1
    for i in range(len(nums) - 1, 0, -1):
        output[len(nums)-i] = output[len(nums)-i] * curr
    # reverse suffix array
    suffix_prod = suffix_prod[::-1]

    # calculate the product except self -> O(n)+O(n) -> O(n)
    for p, s in zip(prefix_prod, suffix_prod):
        output.append(s * p)
    return output

