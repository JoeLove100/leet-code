"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.
"""


def get_hamming_distance(x: int,
                         y: int) -> int:
    bin_x = bin(x)[2:]
    bin_y = bin(y)[2:]
    max_len = max(len(bin_x), len(bin_y))

    bin_x = bin_x.zfill(max_len)
    bin_y = bin_y.zfill(max_len)

    hamming_distance = 0
    for c_x, c_y in zip(bin_x, bin_y):
        if c_x != c_y:
            hamming_distance += 1

    return hamming_distance


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return get_hamming_distance(x, y)