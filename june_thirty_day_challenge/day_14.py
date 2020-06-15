"""
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the
cheapest price from src to dst with up to k stops. If there is no such route, output -1.
"""

import math
from typing import List
from collections import defaultdict


def get_shortest_distance(arr: List[List[int]],
                          k: int,
                          start: int,
                          end: int) -> int:

    adj_map = defaultdict(lambda: [])
    cost_map = dict()
    min_distances = defaultdict(lambda: math.inf)
    min_distances[start] = 0

    for flight in arr:
        adj_map[flight[0]] += [flight[1]]
        cost_map[(flight[0], flight[1])] = flight[2]

    current_nodes = [start]

    for _ in range(k + 1):

        new_min_distances = defaultdict(lambda: math.inf)
        next_nodes = set()

        for node in current_nodes:
            node_weight = min_distances[node]
            all_neighbours = adj_map[node]
            for neighbour in all_neighbours:
                new_distance = node_weight + cost_map[(node, neighbour)]
                new_min_distances[neighbour] = min(new_min_distances[neighbour], new_distance)
                if neighbour not in next_nodes:
                    next_nodes.add(neighbour)

        for node, distance in new_min_distances.items():
            min_distances[node] = min(min_distances[node], distance)

        current_nodes = list(next_nodes)

    if min_distances[end] == math.inf:
        return -1
    else:
        return min_distances[end]


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        return get_shortest_distance(flights, K, src, dst)
