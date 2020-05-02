"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the
number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will
stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1
are happy numbers.
"""


def get_digit_sum_square_2(number):

    total = 0

    while number > 0:
        digit = number % 10
        total += digit ** 2
        number = (number - digit) / 10

    return total


def is_happy(number: int) -> bool:

    visited = set()

    while True:

        number = get_digit_sum_square_2(number)

        if number == 1:
            return True
        elif number in visited:
            return False
        else:
            visited.add(number)


class Solution:
    def isHappy(self, n: int) -> bool:
        return is_happy(n)