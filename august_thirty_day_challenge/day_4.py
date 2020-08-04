"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
"""


def is_power_of_4(num: int) -> bool:

    as_binary = bin(num)[2:]

    if num <= 0:
        return False

    if len(as_binary) % 2 == 0:
        return False

    if any(digit == "1" for digit in as_binary[1:]):
        return False

    return True


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return is_power_of_4(num)
