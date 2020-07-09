"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and
there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One
cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the
perimeter of the island.
"""

from collections import deque
from typing import List, Tuple, Optional


def get_neighbours(coord: Tuple[int, int],
                   grid: List[List[int]]) -> List[Optional[Tuple[int, int]]]:

    neighbours = []
    if coord[0] > 0:
        neighbours.append((coord[0] - 1, coord[1]))
    else:
        neighbours.append(None)
    if coord[0] < len(grid) - 1:
        neighbours.append((coord[0] + 1, coord[1]))
    else:
        neighbours.append(None)
    if coord[1] > 0:
        neighbours.append((coord[0], coord[1] - 1))
    else:
        neighbours.append(None)
    if coord[1] < len(grid[0]) - 1:
        neighbours.append((coord[0], coord[1] + 1))
    else:
        neighbours.append(None)

    return neighbours


def bsf(root: Tuple[int, int],
        grid: List[List[int]]) -> int:

    visited = {root}
    q = deque([root])
    counter = 0

    while q:
        current = q.popleft()
        for next_coord in get_neighbours(current, grid):
            if not next_coord or grid[next_coord[0]][next_coord[1]] == 0:
                counter += 1
            elif next_coord not in visited:
                q.append(next_coord)
                visited.add(next_coord)

    return counter


def get_perimeter(grid: List[List[int]]) -> int:

    if not grid or not grid[0]:
        return 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return bsf((i, j), grid)

    return 0


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return get_perimeter(grid)
