"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly
the town judge.

If the town judge exists, then:

1) The town judge trusts nobody.
2) Everybody (except for the town judge) trusts the town judge.
3_ There is exactly one person that satisfies properties 1 and 2.

You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts
the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
"""

from typing import List


def find_town_judge(n: int,
                    arr: List[List[int]]) -> int:

    trusted_counts = {i + 1: 0 for i in range(0, n)}

    for relation in arr:

        if relation[0] in trusted_counts:
            trusted_counts.pop(relation[0])

        if relation[1] in trusted_counts:
            trusted_counts[relation[1]] += 1

    for person, count in trusted_counts.items():
        if count == n - 1:
            return person

    return -1


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        return find_town_judge(N, trust)
