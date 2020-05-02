import unittest
from april_thirty_day_challenge.day_16 import is_valid


class TestDay16(unittest.TestCase):

    def test_is_valid_blank_text(self):
        # arrange
        text = ""

        # act
        result = is_valid(text)

        # assert
        self.assertTrue(result)

    def test_is_valid_valid_no_stars(self):
        # arrange
        text = "(())()"

        # act
        result = is_valid(text)

        # assert
        self.assertTrue(result)

    def test_is_valid_invalid_no_stars(self):
        # arrange
        text = "(((()))()"

        # act
        result = is_valid(text)

        # assert
        self.assertFalse(result)

    def test_is_valid_one_star_valid(self):
        # arrange
        text = "*"

        # act
        result = is_valid(text)

        # assert
        self.assertTrue(result)

    def test_is_valid_two_stars_valid(self):
        # arrange
        text = "**"

        # act
        result = is_valid(text)

        # assert
        self.assertTrue(result)

    def test_is_valid_not_valid_with_stars(self):
        # arrange
        text = "(*)(*))))"

        # act
        result = is_valid(text)

        # assert
        self.assertFalse(result)

    def test_is_valid_valid_with_stars(self):
        # arrange
        text = "****(((*))"

        # act
        result = is_valid(text)

        # assert
        self.assertTrue(result)

    def test_is_valid_use_start_as_space(self):
        # arrange
        text = "(*)*(*)"

        # act
        result = is_valid(text, )

        # assert
        self.assertTrue(result)

    def test_is_valid(self):
        # arrange
        text = "*)"

        # act
        result = is_valid(text)

        # assert
        self.assertTrue(result)
