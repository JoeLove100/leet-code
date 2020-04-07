import unittest
from thirty_day_challenge.day_7 import get_element_count


class TestDay7(unittest.TestCase):

    def test_get_element_count_empty_array(self):
        # arrange
        arr = []

        # act
        result = get_element_count(arr)

        # assert
        self.assertEqual(0, result)

    def test_get_element_no_repeats(self):
        # arrange
        arr = [1, 2, 3, 7]

        # act
        result = get_element_count(arr)

        # assert
        self.assertEqual(2, result)

    def test_get_element_repeats(self):
        # arrange
        arr = [1, 1, 3, 3, 2, 2, 8, 7]

        # act
        result = get_element_count(arr)

        # assert
        self.assertEqual(5, result)

    def test_get_element_multiple_plus_one(self):
        # arrange
        arr = [1, 3, 2, 3, 5, 0]

        # act
        result = get_element_count(arr)

        # assert
        self.assertEqual(3, result)
