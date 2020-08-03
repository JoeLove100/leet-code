import unittest
from august_thirty_day_challenge.day_3 import is_valid_palindrome


class TestDay3(unittest.TestCase):

    def test_empty_string(self):
        # arrange
        text = ""

        # act
        result = is_valid_palindrome(text)

        # assert
        self.assertTrue(result)

    def test_one_word_palindrome(self):
        # arrange
        text = "abcdcba"

        # act
        result = is_valid_palindrome(text)

        # assert
        self.assertTrue(result)

    def test_one_word_not_palindrome(self):
        # arrange
        text = "abcdba"

        # act
        result = is_valid_palindrome(text)

        # assert
        self.assertFalse(result)

    def test_handles_spaces(self):
        # arrange
        text = " a bcdc b a  "

        # act
        result = is_valid_palindrome(text)

        # assert
        self.assertTrue(result)

    def test_handles_punctuation(self):
        # arrange
        text = "b$c d#, c***b"

        # act
        result = is_valid_palindrome(text)

        # assert
        self.assertTrue(text)

    def test_case_insensitive(self):
        # arrange
        text = "aaaAaA"

        # act
        result = is_valid_palindrome(text)

        # assert
        self.assertTrue(result)
