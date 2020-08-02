import unittest
from july_thirty_day_challenge.day_30 import get_all_words


class TestDay30(unittest.TestCase):

    def test_no_string(self):
        # arrange
        word_dict = ["a", "aba", "bba"]
        s = ""

        # act
        result = get_all_words(s, word_dict)

        # assert
        self.assertSequenceEqual([], result)

    def test_no_words(self):
        # arrange
        word_dict = []
        s = "abdcd"

        # act
        result = get_all_words(s, word_dict)

        # assert
        self.assertSequenceEqual([], result)

    def test_no_solutions(self):
        # arrange
        word_dict = ["a", "b", "c"]
        s = "ababcd"

        # act
        result = get_all_words(s, word_dict)

        # assert
        self.assertSequenceEqual([], result)

    def test_whole_word(self):
        # arrange
        word_dict = ["pear", "apple", "peach"]
        s = "apple"

        # act
        result = get_all_words(s, word_dict)

        # assert
        self.assertSequenceEqual(["apple"], result)

    def test_overlapping_solutions(self):
        # arrange
        word_dict = ["apple", "pen", "applepen", "pine", "pineapple"]
        s = "pineapplepenapple"

        # act
        result = get_all_words(s, word_dict)

        # assert
        expected_result = ["pine apple pen apple", "pine applepen apple", "pineapple pen apple"]
        self.assertSequenceEqual(expected_result, result)
