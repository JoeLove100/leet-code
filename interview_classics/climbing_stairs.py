"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def get_distinct_ways(n: int) -> int:

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n_2 = 1
        n_1 = 1
        for _ in range(n - 1):
            n = n_2 + n_1
            n_2, n_1 = n_1, n

        return n


class Solution:
    def climbStairs(self, n: int) -> int:
        return get_distinct_ways(n)

if __name__ == "__main__":

    print(get_distinct_ways(6))
