import unittest
from july_thirty_day_challenge.day_15 import get_reversed_text


class TestDat15(unittest.TestCase):

    def test_no_words(self):
        # arrange
        text = "   "

        # act
        result = get_reversed_text(text)

        # assert
        self.assertEqual("", result)

    def test_one_word(self):
        # arrange
        text = "cat"

        # act
        result = get_reversed_text(text)

        # assert
        self.assertEqual("cat", result)

    def test_multiple_spaces(self):
        # arrange
        text = "theres     a  cat"

        # act
        result = get_reversed_text(text)

        # assert
        self.assertEqual("cat a theres", result)

    def test_trailing_spaces(self):
        # arrange
        text = "   theres a  cat  "

        # act
        result = get_reversed_text(text)

        # assert
        self.assertEqual("cat a theres", result)

    def test_punctuation(self):
        # arrange
        text = "hello! world!"

        # act
        result = get_reversed_text(text)

        # assert
        self.assertEqual("world! hello!", result)
