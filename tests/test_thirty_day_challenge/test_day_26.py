import unittest
from thirty_day_challenge.day_26 import get_max_substring_length


class TestDay26(unittest.TestCase):

    def test_get_max_substring_same_string(self):
        # arrange
        text_1 = "abcd"
        text_2 = "abcd"

        # act
        result = get_max_substring_length(text_1, text_2)

        # assert
        self.assertEqual(4, result)

    def test_get_max_substring_subset(self):
        # arrange
        text_1 = "abcde"
        text_2 = "cd"

        # act
        result = get_max_substring_length(text_1, text_2)

        # assert
        self.assertEqual(2, result)

    def test_get_max_substring_repeated_letters(self):
        # arrange
        text_1 = "GAGABABA"
        text_2 = "GABA"

        # act
        result = get_max_substring_length(text_1, text_2)

        # assert
        self.assertEqual(4, result)

    def test_get_max_substring_non_contiguous(self):
        # arrange
        text_1 = "RTATRIOP"
        text_2 = "AIGHP"

        # act
        result = get_max_substring_length(text_1, text_2)

        # assert
        self.assertEqual(3, result)

    def test_get_max_substring_repeated_multiple_letters_consecutive(self):
        # arrange
        text_1 = "BAAABGCCC"
        text_2 = "AAXXXC"

        # act
        result = get_max_substring_length(text_1, text_2)

        # assert
        self.assertEqual(3, result)

    def test_get_max_substring_no_substring(self):
        # arrange
        text_1 = "AGR"
        text_2 = "YWF"

        # act
        result = get_max_substring_length(text_1, text_2)

        # assert
        self.assertEqual(0, result)

