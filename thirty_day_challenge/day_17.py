"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded
by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the
grid are all surrounded by water.
"""

from typing import Tuple, List, Set
from collections import deque


class Land:

    def __init__(self):

        self._parents = dict()
        self._ranks = dict()
        self._island_count = 0

    def add(self,
            coord: Tuple[int, int]) -> None:

        self._parents.update({coord: coord})
        self._ranks.update({coord: 0})
        self._island_count += 1

    def find(self,
             coord: Tuple[int, int]) -> Tuple[int, int]:

        if self._parents[coord] != coord:
            self._parents[coord] = self.find(self._parents[coord])

        return self._parents[coord]

    def union(self,
              coord_1: Tuple[int, int],
              coord_2: Tuple[int, int]) -> None:

        if coord_1 not in self._parents or coord_2 not in self._parents:
            return

        parent_1 = self.find(coord_1)
        parent_2 = self.find(coord_2)

        if parent_1 == parent_2:
            return
        else:
            self._island_count -= 1

        if self._ranks[parent_1] < self._ranks[parent_2]:
            self._parents[parent_1] = parent_2
        elif self._ranks[parent_2] < self._ranks[parent_1]:
            self._parents[parent_2] = parent_1
        else:
            self._parents[parent_2] = parent_1
            self._ranks[parent_1] += 1

    def get_number_of_islands(self) -> int:
        return self._island_count

    def get_all_coords(self) -> List[tuple]:
        return list(self._parents)


def get_neighbours(i: int,
                   j: int,
                   length: int,
                   width: int) -> List[Tuple[int, int]]:

    neighbours = []

    if i > 0:
        neighbours.append((i - 1, j))

    if i < length - 1:
        neighbours.append((i + 1, j))

    if j > 0:
        neighbours.append((i, j - 1))

    if j < width - 1:
        neighbours.append((i, j + 1))

    return neighbours


def get_number_of_islands(grid: List[List[str]]) -> int:

    if not grid or not grid[0]:
        return 0

    land = Land()

    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if grid[i][j] != "0":
                land.add((i, j))

    all_coords = land.get_all_coords()
    for coord in all_coords:
        neighbours = get_neighbours(*coord, len(grid), len(grid[0]))
        for n in neighbours:
            land.union(coord, n)

    return land.get_number_of_islands()


def bfs(coord: Tuple[int, int],
        visited: Set,
        grid: List[List[str]]) -> None:

    node_queue = deque([coord])

    while node_queue:
        current = node_queue.popleft()
        neighbours = get_neighbours(*current, len(grid), len(grid[0]))
        for n in neighbours:
            if n not in visited and grid[n[0]][n[1]] != "0":
                node_queue.append(n)
                visited.add(n)


def get_number_of_islands_bfs(grid: List[List[str]]) -> int:

    if not grid or not grid[0]:
        return 0

    island_count = 0
    visited = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if grid[i][j] == "0" and (i, j) not in visited:
                visited.add((i, j))
            elif grid[i][j] != "0" and (i, j) not in visited:
                bfs((i, j), visited, grid)
                island_count += 1

    return island_count


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return get_number_of_islands_bfs(grid)
