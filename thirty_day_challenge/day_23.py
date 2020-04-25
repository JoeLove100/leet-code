"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
"""


def get_binary_and_iterative(start: int,
                             end: int) -> int:

    if end == start:
        return end

    bin_end = bin(end)[2:]
    binary_length = len(bin_end)
    bin_start = bin(start)[2:].zfill(binary_length)

    output = []
    for i in range(binary_length):
        if bin_end[i] == bin_start[i] == "1" and 2 ** (binary_length - (i + 1)) >= end - start:
            output.append("1")
        else:
            output.append("0")

    return int("".join(output), 2)


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        return get_binary_and_iterative(m, n)


if __name__ == "__main__":

    print(get_binary_and_iterative(24, 30))
