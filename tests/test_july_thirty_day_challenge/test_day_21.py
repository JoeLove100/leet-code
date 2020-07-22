import unittest
from july_thirty_day_challenge.day_21 import contains_word


class TestDay21(unittest.TestCase):

    def test_no_word(self):
        # arrange
        arr = [[]]
        word = ""

        # act
        result = contains_word(arr, word)

        # assert
        self.assertTrue(result)

    def test_no_arr(self):
        # arrange
        arr_1 = []
        arr_2 = [[]]
        word = "abc"

        # act
        result_1 = contains_word(arr_1, word)
        result_2 = contains_word(arr_2, word)

        # assert
        self.assertFalse(result_1)
        self.assertFalse(result_2)

    def test_one_row(self):
        # arrange
        arr = [["a", "b", "c", "d"]]
        word = "bc"

        # act
        result = contains_word(arr, word)

        # assert
        self.assertTrue(result)

    def test_one_column(self):
        # arrange
        arr = [["a"], ["b"], ["c"], ["d"]]
        word = "de"

        # act
        result = contains_word(arr, word)

        # assert
        self.assertFalse(result)

    def test_only_use_once(self):
        # arrange
        arr = [["a", "b"], ["c", "d"]]
        word = "aca"

        # act
        result = contains_word(arr, word)

        # assert
        self.assertFalse(result)

    def test_not_straight_line(self):
        # arrange
        arr = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
        word = "ABCCED"

        # act
        result = contains_word(arr, word)

        # assert
        self.assertTrue(result)
