# https://leetcode.com/problems/increasing-triplet-subsequence/


def triplet_exists(nums):
    sol = [float('inf')]*2
    for n in nums:
        if n < sol[0]:
            sol[0] = n
        elif sol[1] > n > sol[0]:
            sol[1] = n
        elif n > sol[1]:
            return True
    return False


nums = [1,2,3,4,5]
# nums = [20, 100, 10, 12, 5, 13]
# nums = [5,4,3,2,1]
# nums = [20,100, 10, 12, 5]
if triplet_exists(nums):
    print("True")
else:
    print("False")


# https://www.youtube.com/watch?v=cjWnW0hdF1Y
# https://leetcode.com/problems/longest-increasing-subsequence/
"""
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""

def longest_increasing_subsequnce_len(nums):
    LIS = [1] * len(nums)

    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
    return max(LIS)

print(longest_increasing_subsequnce_len([10,9,2,5,3,7,101,18]))
print(longest_increasing_subsequnce_len([1,2,4,3]))

# example [1,2,4,3]
# The length of LIS starting at index 3 is 1 because no more elements after it
# The length of LIS starting at index 2 is 1 because 4>3 and no more bigger elements to the right
# len of LIS starting at index 1 is max(LIS[2]+1, LIS[3]+1, 1)
# len of LIS starting at index 0 is max(LIS[1]+1, LIS[2]+1, LIS[3]+1, 1) 1 means ->(just the elem)

def print_longest_increasing_subsequence(nums):
    sols = []

    for i in range(len(nums)):
        if not sols:
            sols.append([nums[i]])
        else:
            for sol in sols:
                if sol[-1] > nums[i] and [nums[i]] not in sols:
                    sols.append([nums[i]])
                elif sol[-1] < nums[i]:
                    sols.append(sol+[nums[i]])
    print(sols)
    max_LIS = []
    for sol in sols:
        if len(max_LIS) < len(sol):
            max_LIS = sol
    print(max_LIS)
    return max_LIS

print_longest_increasing_subsequence([10,9,2,5,3,7,101,18])