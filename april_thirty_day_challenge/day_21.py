"""
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is
sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If
such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

-> BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
-> BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.

Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions
that attempt to circumvent the judge will result in disqualification.
"""
from typing import List


class BinaryMatrix(object):

    def __init__(self,
                 arr: List[List[int]]):

        self._arr = arr

    def get(self, x: int, y: int) -> int:

        return self._arr[x][y]

    def dimensions(self) -> List[int]:

        return [len(self._arr), len(self._arr[0])]


def get_left_most_one(mat: BinaryMatrix) -> int:

    n_rows, n_cols = mat.dimensions()
    row, col = 0, n_cols

    while row < n_rows:
        val = mat.get(row, col - 1)
        if val == 0:
            row += 1
        else:
            col -= 1
            if col == 0:
                break

    if col == n_cols:
        return - 1
    else:
        return col


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: BinaryMatrix) -> int:
        return get_left_most_one(binaryMatrix)
