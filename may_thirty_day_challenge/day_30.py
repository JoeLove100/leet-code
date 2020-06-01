"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
"""

import math
import heapq
from typing import List, Tuple


def get_k_closest_points(all_points: List[List[int]],
                         k: int) -> List[List[int]]:
    if len(all_points) <= k:
        return all_points

    def neg_distance(point: List[int]) -> Tuple[float, int, int]:
        norm = math.sqrt(point[0] ** 2 + point[1] ** 2)
        return -norm, point[0], point[1]

    distances = [neg_distance(point) for point in all_points]
    distance_heap = distances[:k]
    heapq.heapify(distance_heap)

    for i in range(k, len(all_points)):
        if distances[i] > distance_heap[0]:
            heapq.heappop(distance_heap)
            heapq.heappush(distance_heap, distances[i])

    return [[dist[1], dist[2]] for dist in distance_heap]


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return get_k_closest_points(points, K)
