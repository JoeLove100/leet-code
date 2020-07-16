"""
Implement pow(x, n), which calculates x raised to the power n (xn).
"""


def my_pow(x: float,
           n: int) -> float:

    if x == 0:
        return 0

    exponent = abs(n)

    result = 1
    while exponent > 0:
        if exponent % 2 == 0:
            x *= x
            exponent = exponent // 2
        result *= x
        exponent -= 1

    if n < 0:
        return 1 / result
    else:
        return result


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return my_pow(x, n)
