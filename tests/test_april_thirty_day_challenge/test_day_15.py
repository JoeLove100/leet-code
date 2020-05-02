import unittest
from april_thirty_day_challenge.day_15 import get_products


class TestDay15(unittest.TestCase):

    def test_get_products_one_item(self):
        # arrange
        arr = [4]

        # act
        result = get_products(arr)

        # assert
        self.assertSequenceEqual([4], result)

    def test_get_products_two_items(self):
        # arrange
        arr = [4, 3]

        # act
        result = get_products(arr)

        # assert
        self.assertSequenceEqual([3, 4], result)

    def test_get_product_several_items(self):
        # arrange
        arr = [1, 2, 3, 4, 1]

        # act
        result = get_products(arr)

        # assert
        self.assertSequenceEqual([24, 12, 8, 6, 24], result)

    def test_get_product_all_the_same(self):
        # arrange
        arr = [5, 5, 5]

        # act
        result = get_products(arr)

        # assert
        self.assertSequenceEqual([25, 25, 25], result)
