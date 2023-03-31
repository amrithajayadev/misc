def removeDuplicates(nums):
    i = 0
    j = 0
    while nums[i] != '_' and j < len(nums):
        if nums[j] == nums[i]:
            if i != j:
                nums.pop(j)
                nums.append('_')
                i += 1
        j = i + 1

    print(i)
    print(j)
    print(nums)


# removeDuplicates([0, 0, 1, 1, 2, 2, 2, 3, 4, 4, 4])


def remove_duplicates(nums) -> int:
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.pop(i)
        else:
            i += 1
    return nums
# nums = [0,0,1,1,1,2,2,3,3,4]

# nums = [1,1,2]
print(remove_duplicates(nums))