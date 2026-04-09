"""
You're given an array of city pairs and a start city.
You need to find a valid itinerary:
cities = [ ['Milan', 'Mexico'], ['Mexico', 'Dubai'], ['Berlin', 'Milan'], ['Barcelona', 'Berlin'], ]
Having the start: "Barcelona" Here it would be: [ Barcelona, Berlin, Milan, Mexico, Dubai ]
"""
from collections import deque, defaultdict
from typing import List


def build_itinerary(cities):
    parent = {}
    for c1, c2 in cities:
        parent[c2] = c1

    # Find parent using dfs
    def dfs(node):
        if node not in parent:
            return node
        return dfs(parent[node])

    parent = dfs(cities[0][0])
    print(f"Parent :{parent}")

    graph = {}
    for c1, c2 in cities:
        graph[c1] = c2

    q = deque()
    q.append(parent)
    res = []
    while q:
        c = q.popleft()
        if graph.get(c) is not None:
            q.append(graph[c])
        res.append(c)
    return res

cities = [ ['Milan', 'Mexico'], ['Mexico', 'Dubai'], ['Berlin', 'Milan'], ['Barcelona', 'Berlin'], ]
print(f"Parent :{build_itinerary(cities)}")

"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
"""

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    """
    1. Create a graph with src -> (dest,cost) mapping
    2. Create a min_costs array storing the min cost to reach a destination
    3. Use BST to see if the destination is reachable while incrementing the stops at each level
    4. Return the mincost of the dst if the stops is less than k
    """

    mincosts = [float('inf')] * n
    mincosts[src] = 0
    graph = defaultdict(list)
    for c1, c2, cost in flights:
        graph[c1].append((c2, cost))
    print(graph)
    stops = 0
    q = deque()
    q.append((src, 0))
    while q and stops <= k:
        size = len(q)
        for i in range(size):
            cur_city, cur_price = q.popleft()
            for neighbor, price in graph[cur_city]:
                nc = cur_price + price
                if nc < mincosts[neighbor]:
                    mincosts[neighbor] = nc
                    q.append((neighbor, nc))
        stops += 1
    return mincosts[dst] if mincosts[dst] != float('inf') else -1

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(findCheapestPrice(n,flights,src,dst,k))
