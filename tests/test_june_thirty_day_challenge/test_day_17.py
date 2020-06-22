import unittest
from june_thirty_day_challenge.day_17 import get_h_index


class TestDay18(unittest.TestCase):

    def test_one_entry(self):
        # arrange
        arr = [2]

        # act
        result = get_h_index(arr)

        # assert
        self.assertEqual(1, result)

    def test_max_index(self):
        # arrange
        arr = [6, 7, 8, 9, 10]

        # act
        result = get_h_index(arr)

        # assert
        self.assertEqual(5, result)

    def test_zero_citations(self):
        # arrange
        arr = [0, 0, 0, 0]

        # act
        result = get_h_index(arr)

        # assert
        self.assertEqual(0, result)

    def test_multiple_solutions(self):
        # arrange
        arr = [3, 5, 5, 5, 7]

        # act
        result = get_h_index(arr)

        # assert
        self.assertEqual(4, result)

