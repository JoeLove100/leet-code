"""
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which
is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to
finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all
courses, return an empty array.
"""

from typing import List, Set, Dict


def top_sort(i: int,
             visited: Set,
             prev: Set,
             adj_map: Dict[int, List[int]],
             acc: List[int]) -> bool:

    if i in prev:
        return False

    if i not in visited:
        visited.add(i)
        next_courses = adj_map[i]
        for course in next_courses:
            is_dag = top_sort(course, visited, prev | {i}, adj_map, acc)
            if not is_dag:
                return False

        acc.append(i)

    return True


def get_course_order(arr: List[List[int]],
                     n: int) -> List[int]:

    if n == 0:
        return []

    adj_map = dict()
    for i in range(n):
        adj_map[i] = []
    for edge in arr:
        adj_map[edge[1]].append(edge[0])

    visited = set()
    output = []

    for i in adj_map:
        acc = []
        prev = set()
        is_dag = top_sort(i, visited, prev, adj_map, acc)
        if not is_dag:
            return []
        else:
            output.extend(acc)

    return output[::-1]


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return get_course_order(prerequisites, numCourses)
