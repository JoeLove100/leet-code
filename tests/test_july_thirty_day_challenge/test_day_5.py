import unittest
from july_thirty_day_challenge.day_5 import get_hamming_distance


class TestDay5(unittest.TestCase):

    def test_same_number(self):
        # arrange
        x = 1000
        y = 1000

        # act
        result = get_hamming_distance(x, y)

        # assert
        self.assertEqual(0, result)

    def test_different_number(self):
        # arrange
        x = 12
        y = 2

        # act
        result = get_hamming_distance(x, y)

        # assert
        self.assertEqual(3, result)