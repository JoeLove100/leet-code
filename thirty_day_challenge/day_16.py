"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether
this string is valid. We define the validity of a string by these rules:

1) Any left parenthesis '(' must have a corresponding right parenthesis ')'.
2) Any right parenthesis ')' must have a corresponding left parenthesis '('.
3) Left parenthesis '(' must go before the corresponding right parenthesis ')'.
4) '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
5) An empty string is also valid.
"""


def is_valid(text: str):

    bracket_stack = []
    unmatched = [True for _ in range(len(text))]

    for i, character in enumerate(text):

        if character == "(":
            bracket_stack.append(i)
        elif character == ")":
            if not bracket_stack:
                continue
            else:
                open_position = bracket_stack.pop()
                unmatched[open_position] = False
                unmatched[i] = False

    new_text = [text[i] for i in range(len(text)) if unmatched[i]]

    star_stack = []
    open_stack = []
    for t in new_text:
        if t == ")":
            if not star_stack:
                return False
            else:
                star_stack.pop()
        elif t == "(":
            open_stack.append("(")
        else:
            if open_stack:
                open_stack.pop()
            else:
                star_stack.append("*")

    return not open_stack


def is_valid_dp(text: str) -> bool:

    if not text:
        return True

    lefty, righty = "(*", "*)"

    table = [[False for _ in range(len(text))] for _ in range(len(text))]

    for i in range(len(table)):
        if text[i] == "*":
            table[i][i] = True

    for size in range(1, len(text)):
        i = 0
        while i + size < len(text):

            if text[i] == "*" and table[i + 1][i + size]:
                table[i][i + size] = True

            elif text[i] in lefty:
                for k in range(i + 1, i + size + 1):
                    if text[k] in righty:
                        left_correct = k - 1 == i or table[i + 1][k - 1]
                        right_correct = k == i + size or table[k + 1][i + size]
                        if left_correct and right_correct:
                            table[i][i + size] = left_correct and right_correct
                            break

            i += 1

    return table[0][-1]


class Solution:
    def checkValidString(self, s: str) -> bool:
        return is_valid_dp(s)


# if __name__ == "__main__":
#
#     print(is_valid_dp("****("))

if __name__ == "__main__":

    import random
    characters = "()*"

    for _ in range(10000):
        text = "".join([random.choice(characters) for _ in range(10)])
        correct = is_valid(text)
        new = is_valid_dp(text)

        if correct == new:
            print("OK")
        else:
            print(f"Wrong answer for {text}")
            print(f"My answer was {new}")
            print(f"Correct answer is {correct}")
            break
