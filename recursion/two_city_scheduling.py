# https://leetcode.com/problems/two-city-scheduling/description/
from typing import List

# doesn't work
def twoCitySchedCost(costs: List[List[int]]) -> int:
    n = len(costs) // 2

    def _schedule_cost(costs, i, a, b, cost):
        if i == len(costs):
            return cost
        if a == 0 and b == 0:
            return 0
        cost_a = _schedule_cost(costs, i + 1, a - 1, b, cost + costs[i][0])
        cost_b = _schedule_cost(costs, i + 1, a, b - 1, cost + costs[i][1])
        print(cost_a, cost_b, i)
        return min(cost_a, cost_b)

    return _schedule_cost(costs, 0, n, n, 0)


# costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
# costs = [[10, 20],[30, 200]]
# costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# print(twoCitySchedCost(costs))

def two_city_schedule(costs):
    n = len(costs) // 2
    cost_a = [ca for ca,_ in costs]
    diff = [cb-ca for ca, cb in costs]

    cost_b = sum(sorted(diff)[:n])
    return sum(cost_a)+cost_b

costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
# costs = [[10, 20],[30, 200]]
# costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
print(two_city_schedule(costs))