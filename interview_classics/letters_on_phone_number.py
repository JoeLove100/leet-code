"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the
number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1
does not map to any letters.
"""

import itertools
from typing import List


letter_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
              "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


def _get_combos(text: List[str],
                remaining_digits: str,
                output: List[List[str]]):

    if not remaining_digits:
        output.append(text)
    else:
        letters = letter_map[remaining_digits[0]]
        for l in letters:
            t = text.copy()
            t.append(l)
            _get_combos(t, remaining_digits[1:], output)


def get_combos_dfs(digits: str) -> List[str]:

    output = []
    _get_combos([], digits, output)
    return ["".join(s) for s in output]


def get_combos_itertools(number: str) -> List[str]:

    if not number:
        return []

    combos = itertools.product(*[letter_map[n] for n in number])
    output = []
    for c in combos:
        output.append("".join(c))

    return output


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return get_combos_dfs(digits)


if __name__ == "__main__":

    import random
    import cProfile

    random.seed(1234)

    numbers = "".join([str(random.randint(2, 9)) for _ in range(13)])

    cProfile.run(f"get_combos_dfs(str({numbers}))")


