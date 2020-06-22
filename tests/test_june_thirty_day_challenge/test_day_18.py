import unittest
from june_thirty_day_challenge.day_18 import get_longest_duped_string


class TestDay18(unittest.TestCase):

    def test_no_string(self):
        # arrange
        text = ""

        # act
        result = get_longest_duped_string(text)

        # assert
        self.assertEqual("", result)

    def test_no_duplication(self):
        # arrange
        text = "abcfrt"

        # act
        result = get_longest_duped_string(text)

        # assert
        self.assertEqual("", result)

    def test_duplicate_at_end(self):
        # arrange
        text = "abcdfga"

        # act
        result = get_longest_duped_string(text)

        # assert
        self.assertEqual("a", result)

    def test_multiple_dupes(self):
        # arrange
        text = "abcbcab"

        # act
        result = get_longest_duped_string(text)

        # assert
        self.assertEqual("bc", result)

    def test_overlapping_dupes(self):
        # arrange
        text = "banana"

        # act
        result = get_longest_duped_string(text)

        # assert
        self.assertEqual("ana", result)

    def test_all_one_letter(self):
        # arrange
        text = "bbbb"

        # act
        result = get_longest_duped_string(text)

        # assert
        self.assertEqual("bbb", result)
