import unittest
from may_thirty_day_challenge.day_15 import get_max_subarray


class TestDay15(unittest.TestCase):

    def test_get_max_subarray_1_element(self):
        # arrange
        arr = [2]

        # act
        result = get_max_subarray(arr)

        # assert
        self.assertEqual(2, result)

    def test_get_max_subarray_all_positive(self):
        # arrange
        arr = [1, 4, 3, 2, 1]

        # act
        result = get_max_subarray(arr)

        # assert
        self.assertEqual(11, result)

    def test_get_max_subarray_all_negative(self):
        # arrange
        arr = [-5, -2, -1, -2]

        # act
        result = get_max_subarray(arr)

        # assert
        self.assertEqual(-1, result)

    def test_get_max_subarray_max_is_circular(self):
        # arrange
        arr = [5, -3, 2, -1, 5]

        # act
        result = get_max_subarray(arr)

        # assert
        self.assertEqual(11, result)

