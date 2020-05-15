"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number
is the smallest possible.

Note:
-> The length of num is less than 10002 and will be ≥ k.
-> The given num does not contain any leading zero.
"""


def _get_smallest_number_rubbish(n: str,
                                 k: int) -> str:

    pos = 0
    to_remove = []

    while pos + k < len(n) and k > 0:

        min_number = str(min([int(i) for i in n[pos:pos + k + 1]]))

        while n[pos] != min_number:
            to_remove.append(pos)
            pos += 1
            k -= 1

        pos += 1

    to_remove.extend(range(pos, pos + k))

    if len(to_remove) == len(n):
        return "0"
    else:
        number = "".join(n[i] for i in range(len(n)) if i not in to_remove).lstrip("0")
        if number == "":
            return "0"
        else:
            return number


def _get_smallest_number_better(n: str,
                                k: int) -> str:

    number_stack = []

    for c in [int(i) for i in n]:
        if number_stack and number_stack[-1] > c and k > 0:
            number_stack.pop()
            k -= 1

        number_stack.append(c)

    while k > 0:
        number_stack.pop()
        k -= 1

    number = "".join([str(i) for i in number_stack]).lstrip("0")
    return number if number else "0"


def get_smallest_number(n: int,
                        k: int) -> int:

    return int(_get_smallest_number_better(str(n), k))


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        return _get_smallest_number_rubbish(num, k)

