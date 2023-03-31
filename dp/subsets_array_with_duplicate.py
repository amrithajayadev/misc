nums = [4, 4, 4, 1, 4]


def find_subsets(nums, idx, subset, res):
    if subset not in res:
        res.append(subset)

    for i in range(idx, len(nums)):
        find_subsets(nums, i + 1, subset+[nums[i]], res)


def subsets(nums):
    res = []
    find_subsets(sorted(nums), 0, [], res)
    return res


print(subsets(nums))