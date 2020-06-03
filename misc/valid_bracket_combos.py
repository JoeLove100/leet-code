"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

from typing import List


def _is_valid(combo: List[str]) -> bool:

    bracket_stack = []

    for bracket in combo:
        if bracket == "(":
            bracket_stack.append(bracket)
        else:
            if not bracket_stack or bracket_stack.pop() != "(":
                return False

    return True


def _get_combinations(current_combo: List[str],
                      all_combos: List[str],
                      lb_count: int,
                      rb_count: int):

    if not _is_valid(current_combo):
        return

    if lb_count == rb_count == 0:
        all_combos.append("".join(current_combo))
    else:

        if lb_count > 0:
            combo = current_combo.copy()
            combo.append("(")
            _get_combinations(combo, all_combos, lb_count - 1, rb_count)

        if rb_count > 0:
            combo = current_combo.copy()
            combo.append(")")
            _get_combinations(combo, all_combos, lb_count, rb_count - 1)


def get_combinations(n):

    if n == 0:
        return []

    output = []
    _get_combinations([], output, n, n)
    return output


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return get_combinations(n)


if __name__ == "__main__":

    print(len(get_combinations(8)))

