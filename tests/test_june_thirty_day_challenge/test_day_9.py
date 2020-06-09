import unittest
from june_thirty_day_challenge.day_9 import is_subsequence


class TestDay9(unittest.TestCase):

    def test_no_text_or_pattern(self):
        # arrange
        text = ""
        pattern = ""

        # act
        result = is_subsequence(text, pattern)

        # assert
        self.assertTrue(result)

    def test_no_text(self):
        # arrange
        text = ""
        pattern = "abc"

        # act
        result = is_subsequence(text, pattern)

        # assert
        self.assertFalse(result)

    def test_no_pattern(self):
        # arrange
        text = "abc"
        pattern = ""

        # act
        result = is_subsequence(text, pattern)

        # assert
        self.assertTrue(result)

    def test_pattern_longer_than_text(self):
        # arrange
        text = "abc"
        pattern = "abcd"

        # act
        result = is_subsequence(text, pattern)

        # asset
        self.assertFalse(result)

    def test_is_subsequence(self):
        # arrange
        text = "abccddea"
        pattern = "acda"

        # act
        result = is_subsequence(text, pattern)

        # assert
        self.assertTrue(result)

    def test_is_not_subsequence(self):
        # arrange
        text = "abcda"
        pattern = "aed"

        # act
        result = is_subsequence(text, pattern)

        # assert
        self.assertFalse(result)

    def test_are_same(self):
        # arrange
        text = "acgbd"
        pattern = "acgbd"

        # act
        result = is_subsequence(text, pattern)

        # assert
        self.assertTrue(result)
