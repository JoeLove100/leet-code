import unittest
from april_thirty_day_challenge.day_6 import get_anagram_groups


class TestDay6(unittest.TestCase):

    def test_get_anagram_groups_no_anagrams(self):
        # arrange
        arr = ["tes", "tcs", "tbs", "abc"]

        # act
        result = get_anagram_groups(arr)

        # assert
        expected_result = [["tes"], ["tcs"], ["tbs"], ["abc"]]
        self.assertSequenceEqual(expected_result, result)

    def test_get_anagram_groups_all_anagrams(self):
        # arrange
        arr = ["tea", "ate", "eat", "eta"]

        # act
        result = get_anagram_groups(arr)

        # assert
        expected_result = [["tea", "ate", "eat", "eta"]]
        self.assertSequenceEqual(expected_result, result)

    def test_get_anagram_three_groups(self):
        # arrange
        arr = ["eat", "tea", "beat", "ate", "bat", "beta"]

        # act
        result = get_anagram_groups(arr)

        # assert
        expected_result = [["eat", "tea", "ate"], ["beat", "beta"], ["bat"]]
        self.assertSequenceEqual(expected_result, result)

    def test_get_anagram_empty_list(self):
        # arrange
        arr = []

        # act
        result = get_anagram_groups(arr)

        # assert
        self.assertSequenceEqual([], result)

