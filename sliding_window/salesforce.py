# move all 1s to the front
# longest subset that has sum < limit

def rotate(nums):
    i = 0
    j = 0
    n = len(nums)

    while j < n - 1:
        if nums[j] != 1:
            j += 1

        if nums[j] == 1:
            for k in range(j, i, -1):
                nums[k] = nums[k - 1]
            nums[i] = 1
            i += 1
            j += 1
        print(nums)


rotate([2, 3, 5, 1, 3, 4, 1, 5, 3, 9, 1, 3, 0, 1, 8])


def longest_subset_sum(nums, limit):
    i, j = 0, 0
    start, end = 0, 0
    n = len(nums)
    s_sum = 0
    while j < n:
        s_sum += nums[j]

        if s_sum > limit:
            if j - 1 - i > end - start:
                start = i
                end = j-1
            s_sum -= nums[i]
            i += 1
        j += 1
    return nums[start:end+1]


print(longest_subset_sum([2, 3, 5, 1, 1, 1, 1, 1, 3, 4, 1, 5, 3, 9, 1, 3, 0, 1, 8], limit=9))