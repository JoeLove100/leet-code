import unittest
from june_thirty_day_challenge.day_22 import get_single_element


class TestDay22(unittest.TestCase):

    def test_single_element(self):
        # arrange
        arr = [5]

        # act
        result = get_single_element(arr)

        # assert
        self.assertEqual(5, result)

    def test_element_at_end(self):
        # arrange
        arr = [1, 2, 2, 1, 2, 1, 4]

        # act
        result = get_single_element(arr)

        # assert
        self.assertEqual(4, result)

    def test_element_at_start(self):
        # arrange
        arr = [5, 1, 1, 1, 2, 3, 2, 3, 2, 3]

        # act
        result = get_single_element(arr)

        # assert
        self.assertEqual(5, result)

    def test_element_in_middle(self):
        # arrange
        arr = [9, 1, 2, 3, 9, 2, 2, 1, 9, 1]

        # act
        result = get_single_element(arr)

        # assert
        self.assertEqual(3, result)
