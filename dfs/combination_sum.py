from collections import Counter

candidates = [2,3,6,7]
target = 7
Counter

def find_combination(nums, target, path, res):
    if target < 0:
        return
    if target == 0:
        res.append(path)
        return

    for i in range(len(nums)):
        find_combination(nums[i:], target-nums[i], path+[nums[i]], res)


def combination_sum(candidates, target):
    res = []
    find_combination(candidates, target, [], res)
    return res

print(combination_sum(candidates, target))