import unittest
from may_thirty_day_challenge.day_5 import get_index_of_first_unique_letter


class TestDay5(unittest.TestCase):

    def test_get_first_unique_letter_empty_string(self):
        # arrange
        text = ""

        # act
        result = get_index_of_first_unique_letter(text)

        # assert
        self.assertEqual(-1, result)

    def test_get_first_unique_letter_no_unique_letters(self):
        # arrange
        text = "abcdcabdee"

        # act
        result = get_index_of_first_unique_letter(text)

        # assert
        self.assertEqual(-1, result)

    def test_get_first_unique_letter_all_unique(self):
        # arrange
        text = "vbcdefgt"

        # act
        result = get_index_of_first_unique_letter(text)

        # assert
        self.assertEqual(0, result)

    def test_get_first_unique_letter_many_occurences(self):
        # arrange
        text = "aaaba"

        # act
        result = get_index_of_first_unique_letter(text)

        # assert
        self.assertEqual(3, result)

    def test_get_first_unique_letter_first_is_at_end(self):
        # arrange
        text = "aagcbbcgj"

        # act
        result = get_index_of_first_unique_letter(text)

        # assert
        self.assertEqual(8, result)

    def test_get_first_unique_letter_in_middle(self):
        # arrange
        text = "ahdhhaa"

        # act
        result = get_index_of_first_unique_letter(text)

        # assert
        self.assertEqual(2, result)
