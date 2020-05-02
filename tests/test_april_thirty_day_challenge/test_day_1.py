import unittest
from april_thirty_day_challenge.day_1 import get_single_element


class TestDay1(unittest.TestCase):

    def test_get_single_element_two_elements(self):
        # arrange
        arr = [2, 2, 1]

        # act
        result = get_single_element(arr)

        # assert
        self.assertEqual(1, result)

    def test_get_single_element_at_start(self):
        # arrange
        arr = [1, 2, 3, 4, 5, 2, 3, 4, 5]

        # act
        result = get_single_element(arr)

        # assert
        self.assertEqual(1, result)

    def test_get_single_element_in_middle(self):
        # arrange
        arr = [1, 4, 4, 1, 2, 3, 3, 5, 6, 6, 5]

        # act
        result = get_single_element(arr)

        # assert
        self.assertEqual(2, result)





