from collections import deque, defaultdict
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    1. Create dependency graph : sub -> dependencies
    2. Do DFS and note the visited nodes.
    3. If already visited, then return False, else true

    """

    graph = {i: [] for i in range(numCourses)}  # sub -> dependency
    for c1, c2 in prerequisites:
        graph[c1].append(c2)

    visited = set()
    completed = [0] * numCourses

    def dfs(idx):
        if completed[idx] or len(graph[idx]) == 0:
            return True
        visited.add(idx)
        for dep in graph[idx]:
            if completed[dep] == 0 and dep in visited:
                return False
            dfs(dep)
        return True

    for i in range(numCourses):
        if i not in visited and not completed[i]:
            completed[i] = dfs(i)

    return all(completed)


# n = 2
# prerequisites = [[0, 1]]

# n = 6
# prerequisites = [[2,1], [2,3], [1,0], [4,2], [5,2], [5,3]]

# n = 2
# prerequisites = [[0, 1], [1,0]]

n=3
prerequisites = [[0,1],[0,2],[1,2]]
print(canFinish(n, prerequisites))
