
def nextPermutation(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    i = n - 1
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1
    last_peak = i
    print(last_peak)
    if last_peak == 0:
        nums.sort()
        print(nums)
        return nums

    pivot = last_peak - 1

    for i in range(n - 1, pivot, -1):
        if nums[i] > nums[pivot]:
            nums[i], nums[pivot] = nums[pivot], nums[i]
            break
    reverse_suffix(pivot+1, n - 1, nums)
    print(nums)


def reverse_suffix(start, end, nums):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

nextPermutation([1,2,5,3,1])
nextPermutation([1,3,2])
nextPermutation([9,5,4,3,1])
nextPermutation([5,1,1])