import unittest
from may_thirty_day_challenge.day_17 import get_all_anagram_positions


class TestDay17(unittest.TestCase):

    def test_pattern_longer_than_text(self):
        # arrange
        text = "abc"
        pattern = "abcd"

        # act
        result = get_all_anagram_positions(text, pattern)

        # assert
        self.assertSequenceEqual([], result)

    def test_no_anagrams(self):
        # arrange
        text = "aabbccddefg"
        pattern = "ac"

        # act
        result = get_all_anagram_positions(text, pattern)

        # assert
        self.assertSequenceEqual([], result)

    def test_text_and_pattern_are_anagram(self):
        # arrange
        text = "abcba"
        pattern = "bbaca"

        # act
        result = get_all_anagram_positions(text, pattern)

        # assert
        self.assertSequenceEqual([0], result)

    def test_anagram_at_end_of_text(self):
        # arrange
        text = "agfedftss"
        pattern = "sts"

        # act
        result = get_all_anagram_positions(text, pattern)

        # assert
        self.assertSequenceEqual([6], result)

    def test_all_one_letter(self):
        # arrange
        text = "aaaaa"
        pattern = "aa"

        # act
        result = get_all_anagram_positions(text, pattern)

        # assert
        self.assertSequenceEqual([0, 1, 2, 3], result)

    def test_multiple_anagrams(self):
        # arrange
        text = "abab"
        pattern = "ab"

        # act
        result = get_all_anagram_positions(text, pattern)

        # assert
        self.assertSequenceEqual([0, 1, 2], result)
