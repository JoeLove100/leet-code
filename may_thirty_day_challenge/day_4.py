"""
Given a positive integer, output its complement number. The complement strategy is to flip
the bits of its binary representation.
"""


def get_binary_complement(n: int) -> int:

    bin_number = bin(n)[2:]
    complement = 0

    for i, c in enumerate(reversed(bin_number)):
        if c == "0":
            complement += 2 ** i

    return complement


class Solution:
    def findComplement(self, num: int) -> int:
        return get_binary_complement(num)
