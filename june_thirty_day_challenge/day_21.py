"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The
dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in
the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops
to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these
rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's
health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or
downward in each step.
"""

from typing import List


def get_min_health_points(dungeon: List[List[int]]) -> int:

    if not dungeon or not dungeon[0]:
        return 1

    dp = [[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]

    for i in reversed(range(len(dungeon))):
        for j in reversed(range(len(dungeon[0]))):

            if i == len(dungeon) - 1 and j == len(dungeon[0]) - 1:
                dp[i][j] = max(-dungeon[i][j] + 1, 1)
            elif i == len(dungeon) - 1:
                dp[i][j] = max(-dungeon[i][j] + dp[i][j + 1], 1)
            elif j == len(dungeon[0]) - 1:
                dp[i][j] = max(-dungeon[i][j] + dp[i + 1][j], 1)
            else:
                dp[i][j] = max(-dungeon[i][j] + min(dp[i + 1][j], dp[i][j + 1]), 1)

    return dp[0][0]


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
            return get_min_health_points(dungeon)
