import unittest
from may_thirty_day_challenge.day_12 import get_single_element


class TestDay12(unittest.TestCase):

    def test_get_single_element_one_element(self):
        # arrange
        arr = [2]

        # act
        result = get_single_element(arr)

        # assert
        self.assertEqual(2, result)

    def test_get_single_element_lower_half(self):
        # arrange
        arr = [1, 1, 3, 4, 4, 5, 5, 6, 6, 9, 9]

        # act
        result = get_single_element(arr)

        # assert
        self.assertEqual(3, result)

    def test_get_single_element_upper_half(self):
        # arrange
        arr = [1, 1, 3, 3, 4, 4, 5, 5, 6, 9, 9]

        # act
        result = get_single_element(arr)

        # assert
        self.assertEqual(6, result)

    def test_get_single_element_at_start(self):
        # arrange
        arr = [4, 5, 5, 7, 7]

        # act
        result = get_single_element(arr)

        # assert
        self.assertEqual(4, result)

    def test_get_single_element_at_end(self):
        # arrange
        arr = [4, 4, 5, 5, 7]

        # act
        result = get_single_element(arr)

        # assert
        self.assertEqual(7, result)
