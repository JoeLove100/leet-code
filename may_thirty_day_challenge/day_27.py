"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.
"""
from typing import List
from collections import defaultdict, deque


def can_be_partitioned(n: int,
                       dislikes: List[List[int]]):

    vertices = defaultdict(lambda: [])

    for v in dislikes:
        vertices[v[0]].append(v[1])
        vertices[v[1]].append(v[0])

    visited = dict()

    for i in range(1, n + 1):
        if i in visited:
            continue

        q = deque([i])
        visited[i] = "w"
        counter = 1
        while q:
            nodes_on_level = len(q)
            current_colour = "b" if counter % 2 == 1 else "w"

            while nodes_on_level > 0:
                current_node = q.popleft()
                for next_node in vertices[current_node]:
                    if next_node in visited:
                        if visited[next_node] != current_colour:
                            return False
                    else:
                        visited[next_node] = current_colour
                        q.append(next_node)

                nodes_on_level -= 1

            counter += 1

    return True


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        return can_be_partitioned(N, dislikes)
