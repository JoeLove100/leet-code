import unittest
from may_thirty_day_challenge.day_18 import contains_permutation


class TestDay18(unittest.TestCase):

    def test_pattern_longer_than_text(self):
        # arrange
        s_1 = "abcd"
        s_2 = "abc"

        # act
        result = contains_permutation(s_1, s_2)

        # assert
        self.assertFalse(result)

    def test_pattern_contained_exactly(self):
        # arrange
        s_1 = "ab"
        s_2 = "gbbcdfab"

        # act
        result = contains_permutation(s_1, s_2)

        # assert
        self.assertTrue(result)

    def test_pattern_contains_permutation(self):
        # arrange
        s_1 = "aba"
        s_2 = "gaaaaabcdff"

        # act
        result = contains_permutation(s_1, s_2)

        # assert
        self.assertTrue(result)

