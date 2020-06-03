"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""


def is_valid(text: str):

    bracket_pairs = {")": "(", "}": "{", "]": "["}
    bracket_stack = []

    for b in text:
        if b not in bracket_pairs:
            bracket_stack.append(b)
        else:
            if len(bracket_stack) == 0 or bracket_pairs[b] != bracket_stack.pop():
                return False

    return len(bracket_stack) == 0


class Solution:
    def isValid(self, s: str) -> bool:
        return is_valid(s)


if __name__ == "__main__":

    t = "]]]]"
    print(is_valid(t))
