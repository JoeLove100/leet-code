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


def _is_perfect_square_binary_search(n: int,
                                    low: int,
                                    high: int) -> bool:

    if low >= high:
        return False

    mid = int((low + high) // 2)
    guess = mid ** 2

    if guess == n:
        return True
    elif guess > n:
        return _is_perfect_square_binary_search(n, low, mid)
    else:
        return _is_perfect_square_binary_search(n, mid + 1, high)


def is_perfect_square_binary_search(n: int) -> bool:

    if n == 1:
        return True

    return _is_perfect_square_binary_search(n, 0, n)


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return is_perfect_square(num)
