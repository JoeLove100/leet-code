import unittest
from august_thirty_day_challenge.day_1 import is_correct_caps


class TestDay1(unittest.TestCase):

    def test_no_word(self):
        # arrange
        word = ""

        # act
        result = is_correct_caps(word)

        self.assertTrue(result)

    def test_one_letter(self):
        # arrange
        word = "A"

        # act
        result = is_correct_caps(word)

        # assert
        self.assertTrue(result)

    def test_all_caps(self):
        # arrange
        word = "TESTING"

        # act
        result = is_correct_caps(word)

        # assert
        self.assertTrue(result)

    def test_all_lower(self):
        # arrange
        word = "testing"

        # act
        result = is_correct_caps(word)

        # assert
        self.assertTrue(result)

    def test_first_upper(self):
        # arrange
        word = "Testing"

        # act
        result = is_correct_caps(word)

        # arrange
        self.assertTrue(result)

    def test_wrong_first_upper(self):
        # arrange
        word = "TesTing"

        # act
        result = is_correct_caps(word)

        # assert
        self.assertFalse(result)

    def test_wrong_first_lower(self):
        # arrange
        word = "bE"

        # act
        result = is_correct_caps(word)

        # assert
        self.assertFalse(result)
