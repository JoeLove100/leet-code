import unittest
from june_thirty_day_challenge.day_16 import set_board


class TestDay16(unittest.TestCase):

    def test_empty_arr(self):
        # arrange
        arr_1 = []
        arr_2 = [[]]

        # act
        set_board(arr_1)
        set_board(arr_2)

        # assert
        self.assertSequenceEqual([], arr_1)
        self.assertSequenceEqual([[]], arr_2)

    def test_single_row(self):
        # arrange
        arr = [["X", "O", "X", "O"]]

        # act
        set_board(arr)

        # assert
        self.assertSequenceEqual([["X", "O", "X", "O"]], arr)

    def test_single_column(self):
        # arrange
        arr = [["X"], ["O"], ["X"], ["X"]]

        # act
        set_board(arr)

        # assert
        self.assertSequenceEqual([["X"], ["O"], ["X"], ["X"]], arr)

    def test_all_x(self):
        # arrange
        arr = [["X", "X", "X"], ["X", "X", "X"]]

        # act
        set_board(arr)

        # assert
        self.assertSequenceEqual([["X", "X", "X"], ["X", "X", "X"]], arr)

    def test_all_o(self):
        # arrange
        arr = [["O", "O"], ["O", "O"]]

        # act
        set_board(arr)

        # assert
        self.assertSequenceEqual( [["O", "O"], ["O", "O"]], arr)

    def test_mixed(self):
        # arrange
        arr = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

        # act
        set_board(arr)

        # assert
        expected_result = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
        self.assertSequenceEqual(expected_result, arr)
