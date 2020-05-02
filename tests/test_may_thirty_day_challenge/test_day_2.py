import unittest
from may_thirty_day_challenge.day_2 import get_number_of_jewels


class TestDay2(unittest.TestCase):

    def test_get_number_of_jewels_no_jewels(self):
        # arrange
        J = ""
        S = "abdcdca"

        # act
        result = get_number_of_jewels(J, S)

        # assert
        self.assertEqual(0, result)

    def test_get_number_of_jewels_no_stones(self):
        # arrange
        J = "abc"
        S = ""

        # act
        result = get_number_of_jewels(J, S)

        # assert
        self.assertEqual(0, result)

    def test_get_number_of_jewels_no_intersection(self):
        # arrange
        J = "abc"
        S = "ABCABC"

        # act
        result = get_number_of_jewels(J, S)

        # assert
        self.assertEqual(0, result)

    def test_get_number_of_jewels(self):
        # arrange
        J = "aBc"
        S = "cCaAghfbBghfB"

        # act
        result = get_number_of_jewels(J, S)

        # assert
        self.assertEqual(4, result)
