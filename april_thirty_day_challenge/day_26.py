

def get_max_substring_length(text_1: str,
                             text_2: str) -> int:

    if not text_1 or not text_2:
        return 0

    tab = [[0 for _ in range(len(text_1) + 1)] for _ in range(len(text_2) + 1)]

    for i in range(len(text_2) - 1, -1, -1):
        for j in range(len(text_1) - 1, -1, -1):

            right = tab[i + 1][j]
            down = tab[i][j + 1]
            diag = tab[i + 1][j + 1] + (text_1[j] == text_2[i])
            tab[i][j] = max(right, down, diag)

    return tab[0][0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return get_max_substring_length(text1, text2)
