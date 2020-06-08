"""
Given an integer, write a function to determine if it is a power of two.
"""


def is_power_of_2(n: int) -> bool:

    if n < 1:
        return False

    while n > 1:

        if n % 2 == 1:
            return False

        n = n // 2

    return True


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return is_power_of_2(n)
