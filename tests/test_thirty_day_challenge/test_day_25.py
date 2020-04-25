import unittest
from thirty_day_challenge.day_25 import is_possible, is_possible_linear


class TestDay25(unittest.TestCase):

    def test_is_possible_empty_array(self):
        # arrange
        arr = []

        # act
        result = is_possible_linear(arr)

        # assert
        self.assertTrue(result)

    def test_is_possible_array_length_one(self):
        # arrange
        arr = []

        # act
        result = is_possible_linear(arr)

        # assert
        self.assertTrue(result)

    def test_is_possible_larger_jump_than_array_length(self):
        # arrange
        arr = [2, 10, 1, 3]
        
        # act
        result = is_possible_linear(arr)

        # assert
        self.assertTrue(result)

    def test_is_possible_not_possible(self):
        # arrange
        arr = [3, 2, 1, 0, 4]
        
        # act
        result = is_possible_linear(arr)

        # assert
        self.assertFalse(result)

    def test_is_possible_is_possible(self):
        # arrange
        arr = [2, 3, 1, 1, 4]
        
        # act
        result = is_possible_linear(arr)

        # assert
        self.assertTrue(result)
