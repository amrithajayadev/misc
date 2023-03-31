# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
import math


def min_fuel_cost(roads, seats):
    graph = {i: [] for i in range(len(roads) + 1)}
    fuel = 0
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, parent):
        nonlocal fuel
        num_people = 0
        for child in graph[node]:
            if child != parent:
                p = dfs(child, node)
                num_people += p
                fuel += math.ceil(num_people / seats)
        return num_people + 1

    dfs(0, -1)
    return fuel


roads = [[0, 1], [0, 2], [0, 3]]
seats = 5
print(min_fuel_cost(roads, seats))
