"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you
have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have
are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
so "a" is considered a different type of stone from "A".
"""


def get_number_of_jewels(J: str,
                         S: str) -> int:

    jewels = set(J)
    jewel_count = 0

    for stone in S:
        if stone in jewels:
            jewel_count += 1

    return jewel_count


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return get_number_of_jewels(J, S)
