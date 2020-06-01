import unittest
from may_thirty_day_challenge.day_31 import min_changes


class TestDay31(unittest.TestCase):

    def test_no_word_1(self):
        # arrange
        word_1 = ""
        word_2 = "asc"

        # act
        result = min_changes(word_1, word_2)

        # assert
        self.assertEqual(3, result)

    def test_no_word_2(self):
        # arrange
        word_1 = "asc"
        word_2 = ""

        # act
        result = min_changes(word_1, word_2)

        # assert
        self.assertEqual(3, result)

    def test_same_word(self):
        # arrange
        word_1 = "abcd"
        word_2 = "abcd"

        # act
        result = min_changes(word_1, word_2)

        # assert
        self.assertEqual(0, result)

    def test_different_word(self):
        # arrange
        word_1 = "intention"
        word_2 = "execution"

        # act
        result = min_changes(word_1, word_2)

        # assert
        self.assertEqual(5, result)
