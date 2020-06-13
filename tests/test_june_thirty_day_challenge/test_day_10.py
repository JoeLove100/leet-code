import unittest
from june_thirty_day_challenge.day_10 import binary_search


class TestDay10(unittest.TestCase):

    def test_smaller_than_all(self):
        # arrange
        arr = [1, 5, 6, 8, 10]
        target = -1

        # act
        result = binary_search(arr, target)

        # assert
        self.assertEqual(0, result)

    def test_greater_than_all(self):
        # arrange
        arr = [1, 5, 6, 8, 11]
        target = 20

        # act
        result = binary_search(arr, target)

        # assert
        self.assertEqual(5, result)

    def test_not_contained(self):
        # arrange
        arr = [1, 5, 6, 8, 11]
        target = 3

        # act
        result = binary_search(arr, target)

        # act
        self.assertEqual(1, result)

    def test_contained(self):
        # arrange
        arr = [1, 5, 6, 8, 11]
        target = 11

        # act
        result = binary_search(arr, target)

        # assert
        self.assertEqual(4, result)
