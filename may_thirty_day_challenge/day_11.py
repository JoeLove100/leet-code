"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the
image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel
value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the
starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those
pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned
pixels with the newColor.

At the end, return the modified image.
"""

from typing import List, Set, Tuple
from collections import deque


def _get_neighbours(coord: Tuple[int, int],
                    length: int,
                    width: int) -> List[Tuple[int, int]]:
    neighbours = []
    if coord[0] < length - 1:
        neighbours.append((coord[0] + 1, coord[1]))
    if coord[0] > 0:
        neighbours.append((coord[0] - 1, coord[1]))
    if coord[1] < width - 1:
        neighbours.append((coord[0], coord[1] + 1))
    if coord[1] > 0:
        neighbours.append((coord[0], coord[1] - 1))

    return neighbours


def _fill(arr: List[List[int]],
          root: Tuple[int, int],
          new_colour: int,
          visited: Set[Tuple[int, int]]) -> None:

    if not arr or not arr[0]:
        return

    node_q = deque([root])
    val = arr[root[0]][root[1]]

    while node_q:

        current = node_q.popleft()
        if current in visited:
            continue

        arr[current[0]][current[1]] = new_colour
        visited.add(current)

        for neighbour in _get_neighbours(current, len(arr), len(arr[0])):
            if arr[neighbour[0]][neighbour[1]] == val:
                node_q.append(neighbour)


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        _fill(image, (sr, sc), newColor, set())
        return image

