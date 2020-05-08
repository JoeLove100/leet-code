"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate
of a point. Check if these points make a straight line in the XY plane.
"""

from typing import List
import math


def get_gradient(coord_1,
                 coord_2) -> float:

    if coord_1[0] == coord_2[0]:
        return math.inf
    elif coord_1[0] < coord_2[0]:
        return (coord_2[1] - coord_1[1]) / (coord_2[0] - coord_1[0])
    else:
        return (coord_1[1] - coord_2[1]) / (coord_1[0] - coord_2[0])


def are_colinear(coords: List[List[int]]):

    initial_grad = get_gradient(coords[0], coords[1])

    for i in range(2, len(coords)):

        grad = get_gradient(coords[0], coords[i])
        if grad != initial_grad:
            return False

    return True


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        return are_colinear(coordinates)
