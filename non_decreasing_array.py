def checkPossibility(nums) -> bool:
    changed = False
    for i in range(len(nums)-1):
        if nums[i] <= nums[i + 1]:
            continue
        if changed:
            return False
        if i == 0 or nums[i + 1] >= nums[i - 1]:
            nums[i] = nums[i + 1]
        else:
            nums[i + 1] = nums[i]
        changed = True
        print(nums)
    return True


# nums = [4, 2, 3]  # -> [0, -2, 1]
# nums = [4,2,1] # -> [0, -2, -1]
# nums = [1, 2, 2, 1, 4, 5] # ->[0,1,0,-1,3,1]
# nums = [3, 4, 2, 3]  # -> [0,1,-2,1]
# nums = [-1,4,2,3] # ->[0,5,-2,1]
nums = [1,4,1,2]
if checkPossibility(nums):
    print("true")
else:
    print("false")