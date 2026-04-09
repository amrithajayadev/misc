"""
    The maximum distance attainable between the balls in the given positions is
    upper_limit = pos[-1] - pos[0] // num_balls -1
    So we start checking each values between 1 and upper_limit and check which is feasible using binary search.
    if not possible, hi -= 1
    if possible, store the value, try higer value lo+= 1
    Feasibility check
    - place the ball in arr[0]
    - check the distance between balls between (1,n-1).
    - if distance >
    """
from typing import List


def maxDistance(position: List[int], m: int) -> int:
    position.sort()  # O(nlogn)
    n = len(position)
    l = 1
    r = (position[n - 1] - position[0]) // (m - 1)
    max_dist = 0

    def isFeasible(dist):
        count = 1
        lastPlaced = position[0]
        for i in range(1, n):
            print(f"dist={dist}, diff={position[i] - lastPlaced}")
            if position[i] - lastPlaced >= dist:
                count += 1
                lastPlaced = position[i]
            if count >= m:
                print(f"at lastPlaced={lastPlaced} and count={count}")
                return True
        return False

    while l <= r:
        mid = (l + r) // 2
        if isFeasible(mid):
            max_dist = mid
            l = mid + 1
        else:
            r = mid - 1
    return max_dist


arr = [5, 4, 3, 2, 1, 1000000000]
balls = 2
print(maxDistance(arr, balls))
