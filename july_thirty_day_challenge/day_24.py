"""
Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them
in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for
 which the edge (i, j) exists.
"""

from typing import List


def get_all_paths(arr: List[List[int]]) -> List[List[int]]:

    paths_by_node = {i: [] for i in range(len(arr))}
    paths_by_node[len(arr) - 1].append([len(arr) - 1])

    for i in reversed(range(len(arr) - 1)):
        paths = []
        successors = arr[i]

        for j in successors:
            for path_segment in paths_by_node[j]:
                paths.append(path_segment + [i])

        paths_by_node[i].extend(paths)

    return [p[::-1] for p in paths_by_node[0]]


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return get_all_paths(graph)
