"""
p0 ----mid--p2---n

"""


def sortZeroOneTwo(nums):
    p0 = 0
    p2 = len(nums) - 1
    p1 = 0
    while p0 <= p2 and p1 <= p2:
        mid = (p1 + p2) // 2
        print(p0, p1, p2, mid)
        if nums[mid] == 0:
            nums[p0], nums[mid] = nums[mid], nums[p0]
            p0 += 1
        elif nums[mid] == 2:
            nums[p2], nums[mid] = nums[mid], nums[p2]
            p2 -= 1
        elif nums[mid] == 1:
            if p1 <= p0:
                p1 = p0 + 1
            if nums[p1] == 1:
                p1 = p1 + 1
        print(nums)


# nums = [1, 0, 0, 2, 1]
# nums = [1,1,1,0,2]
# nums = [1,1,1,2]
# nums = [1,2,2,2,0]
nums = [2,0,2,1,1,0]
sortZeroOneTwo(nums)
