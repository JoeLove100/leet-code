import unittest
from april_thirty_day_challenge.day_27 import get_max_area


class Testay27(unittest.TestCase):

    def test_get_max_area_empty(self):
        # arrange
        arr_1 = []
        arr_2 = [[]]

        # act
        result_1 = get_max_area(arr_1)
        result_2 = get_max_area(arr_2)

        # assert
        self.assertEqual(0, result_1)
        self.assertEqual(0, result_2)

    def test_get_max_area_all_zero(self):
        # arrange
        arr = [["0", "0", "0"], ["0", "0", "0"]]

        # act
        result = get_max_area(arr)

        # assert
        self.assertEqual(0, result)

    def test_get_max_area_column(self):
        # arrange
        arr = [["1"], ["1"], ["1"], ["0"]]

        # act
        result = get_max_area(arr)

        # assert
        self.assertEqual(1, result)

    def test_get_max_area_row(self):
        # arrange
        arr = [["1", "0", "1", "1"]]

        # act
        result = get_max_area(arr)

        # assert
        self.assertEqual(1, result)

    def test_get_max_area_max_two(self):
        # arrange
        arr = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
               ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]

        # act
        result = get_max_area(arr)

        # assert
        self.assertEqual(4, result)

    def test_get_max_area_max_three(self):
        #
        arr = [["1", "0", "0", "0"], ["0", "1", "1", "1"], ["0", "1", "1", "1"], ["0", "1", "1", "1"]]

        # act
        result = get_max_area(arr)

        # assert
        self.assertEqual(9, result)

