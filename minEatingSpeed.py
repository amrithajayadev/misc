from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    piles.sort()
    lo = piles[0]
    hi = piles[-1]
    ans = 0

    def canEat(rate):
        hours = 0
        total = sum(piles)
        for p in piles:
            print(f"Total:{total}, processing p:{p}, rate:{rate}, updated total ={total - min(p, rate)}, h={hours}")
            total = total - p
            num_hours = (p // rate) if (p // rate) > 0 else 1
            hours = hours + num_hours
            if total <= 0 and hours < h:
                print(f"Found the rate: {rate}")
                return True
        return False

    while lo <= hi:
        mid = (lo + hi) // 2
        if canEat(mid):
            ans = max(mid, ans)
            hi = mid - 1
        else:
            lo = mid + 1
    return ans

piles = [25,10,23,4]
h = 4

# piles=[1,4,3,2]
# h=9
print(minEatingSpeed(piles, h))