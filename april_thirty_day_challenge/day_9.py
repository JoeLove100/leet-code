"""
Given two strings S and T, return if they are equal when both are typed into empty text
editors. # means a backspace character.
"""


def get_next_char_index(text: str,
                        current_index) -> int:

    backspace_count = 0
    while current_index >= 0 and text[current_index] == "#":
        backspace_count += 1
        current_index -= 1

        while backspace_count > 0:
            if text[current_index] == "#":
                break
            else:
                backspace_count -= 1
                current_index -= 1

    return current_index


def are_same(text_1: str,
             text_2: str) -> bool:

    i = len(text_1) - 1
    j = len(text_2) - 1

    while True:

        i = get_next_char_index(text_1, i)
        j = get_next_char_index(text_2, j)

        if i < 0 and j < 0:
            return True
        elif text_1[i] != text_2[j]:
            return False
        else:
            i -= 1
            j -= 1


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return are_same(S, T)


if __name__ == "__main__":

    print(are_same("abcd#", "abc"))


