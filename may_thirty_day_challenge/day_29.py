"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is
expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
"""
from typing import List
from collections import defaultdict


def is_possible(prereq: List[List[int]],
                n: int) -> bool:

    vertices = defaultdict(lambda: [])

    for courses in prereq:
        vertices[courses[0]] += [courses[1]]

    visited = set()

    for i in range(n):
        if i in visited:
            continue

        current = i
        stack = []
        while True:
            if not vertices[current]:
                if stack:
                    current = stack.pop()
                else:
                    break
            else:
                stack.append(current)
                current = vertices[current].pop()
                visited.add(current)
                if current in stack:
                    return False

    return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return is_possible(prerequisites, numCourses)
