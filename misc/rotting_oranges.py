"""
In a given grid, each cell can have one of three values:

-> the value 0 representing an empty cell;
-> the value 1 representing a fresh orange;
-> the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this
is impossible, return -1 instead.
"""

from typing import List, Tuple
from collections import deque


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


def get_minutes_to_rot(oranges: List[List[int]]):

    if not oranges or not oranges[0]:
        # null grid edge case
        return 0

    visited = set()
    node_queue = deque()
    fresh_orange_count = 0
    minutes = 0

    for i in range(len(oranges)):
        for j in range(len(oranges[0])):

            if oranges[i][j] == 1:
                fresh_orange_count += 1
            elif oranges[i][j] == 2:
                node_queue.append((i, j))
                visited.add((i, j))

    if fresh_orange_count == 0:
        # no oranges to rot...
        return 0

    while True:
        counter = len(node_queue)
        while counter > 0:
            current = node_queue.popleft()
            neighbours = get_neighbours(*current, len(oranges), len(oranges[0]))
            for node in neighbours:
                if node not in visited:
                    visited.add(node)
                    if oranges[node[0]][node[1]] == 1:
                        node_queue.append(node)
                        fresh_orange_count -= 1

            counter -= 1

        if node_queue:
            minutes += 1
        else:
            break

    if fresh_orange_count > 0:
        return - 1
    else:
        return minutes


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        return get_minutes_to_rot(grid)


if __name__ == "__main__":

    arr = [[0, 2]]
    print(get_minutes_to_rot(arr))
