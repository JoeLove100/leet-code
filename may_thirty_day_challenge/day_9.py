"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.
"""


def is_perfect_square(n: int) -> bool:

    if n <= 0:
        return False

    k = 1
    while True:
        div = n / k
        if div < k:
            return False
        elif div == k:
            return True
        else:
            k += 1


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return is_perfect_square(num)
