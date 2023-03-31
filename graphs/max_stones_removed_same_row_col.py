# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
from typing import List


def removeStones(stones: List[List[int]]) -> int:
    graph = {}
    visited = set()

    for x, y in stones:
        if (x,y) not in graph:
            if x in



    print(graph)


stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
removeStones(stones)