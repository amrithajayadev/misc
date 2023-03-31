# https://leetcode.com/problems/intervals-between-identical-elements/
from collections import defaultdict


def intervals_identical_arrays(nums):
    pos = defaultdict(list)
    for i, n in enumerate(nums):
        pos[n].append(i)

    res = [-1] * len(nums)
    for _, idxs in pos:
        for i in idxs:
            res[i] = sum(idxs) - i * (len(idxs) - 1)