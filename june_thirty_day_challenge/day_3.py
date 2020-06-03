"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0],
and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
"""

import heapq
from typing import List


def get_min_cost(all_costs: List[List[int]]) -> int:

    min_cost = 0
    city_a = []
    city_b = []

    for cost in all_costs:
        if cost[0] < cost[1]:
            min_cost += cost[0]
            city_a.append(cost[1] - cost[0])
        else:
            min_cost += cost[1]
            city_b.append(cost[0] - cost[1])

    if len(city_a) > len(all_costs) // 2:
        heapq.heapify(city_a)
        for _ in range(len(city_a) - len(all_costs) // 2):
            min_cost += heapq.heappop(city_a)

    if len(city_b) > len(all_costs) // 2:
        heapq.heapify(city_b)
        for _ in range(len(city_b) - len(all_costs) // 2):
            min_cost += heapq.heappop(city_b)

    return min_cost


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        return get_min_cost(costs)
