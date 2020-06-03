"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).
"""
from typing import List


def rotate_matrix(mat: List[List[int]],
                  start: int,
                  end: int) -> None:
    """
    rotate matrix 90 degrees in place
    """

    if end - start <= 1:
        return

    old_first_row = [mat[start][i] for i in range(start, end)]
    old_last_row = [mat[end - 1][i] for i in range(start, end)]
    old_first_col = [mat[i][start] for i in range(start, end)]
    old_last_col = [mat[i][end - 1] for i in range(start, end)]

    mat[start][start:end] = old_first_col[::-1]
    mat[end - 1][start:end] = old_last_col[::-1]

    for i in range(start, end):
        mat[i][end - 1] = old_first_row[i - start]
        mat[i][start] = old_last_row[i - start]

    rotate_matrix(mat, start + 1, end - 1)


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        else:
            rotate_matrix(matrix, 0, len(matrix))


def print_matrix(mat: List[List[int]]) -> None:

    for row in mat:
        print(", ".join([str(n) for n in row]))


if __name__ == "__main__":

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate_matrix(matrix, 0, len(matrix))
    print_matrix(matrix)

