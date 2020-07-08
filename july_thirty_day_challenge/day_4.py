"""
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
Notes:
    -> 1 is an ugly number
    -> n is less than 1690
"""


def get_nth_ugly_number(n: int) -> int:

    ugly_numbers = [1]
    i_2 = i_3 = i_5 = 0

    while len(ugly_numbers) < n:

        next_ugly_number = min(2 * ugly_numbers[i_2], 3 * ugly_numbers[i_3], 5 * ugly_numbers[i_5])
        ugly_numbers.append(next_ugly_number)
        if next_ugly_number == 2 * ugly_numbers[i_2]:
            i_2 += 1
        if next_ugly_number == 3 * ugly_numbers[i_3]:
            i_3 += 1
        if next_ugly_number == 5 * ugly_numbers[i_5]:
            i_5 += 1

    return ugly_numbers[-1]


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return get_nth_ugly_number(n)
