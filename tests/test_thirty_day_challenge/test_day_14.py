import unittest
from thirty_day_challenge.day_14 import get_shifted_text, get_shifted_text_2


class TestDay14(unittest.TestCase):

    def test_shift_right(self):
        # arrange
        text = "abcd"

        # act
        result = get_shifted_text_2(text, [[1, 2]])

        # assert
        self.assertEqual("cdab", result)

    def test_shift_left(self):
        # arrange
        text = "abcd"

        # act
        result = get_shifted_text_2(text, [[0, 1]])

        # assert
        self.assertEqual("bcda", result)

    def test_both_shifts(self):
        # arrange
        text = "abcd"

        # act
        result = get_shifted_text_2(text, [[1, 3], [0, 1]])

        # assert
        self.assertEqual("cdab", result)
