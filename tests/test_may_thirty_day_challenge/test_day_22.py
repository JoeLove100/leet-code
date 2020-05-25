import unittest
from may_thirty_day_challenge.day_22 import sort_letters


class TestDay22(unittest.TestCase):

    def test_no_text(self):
        # arrange
        text = ""

        # act
        result = sort_letters(text)

        # assert
        self.assertEqual("", result)

    def test_sort_letters_all_occur_once(self):
        # arrange
        text = "abcde"

        # act
        result = sort_letters(text)

        # assert
        self.assertEqual("abcde", result)

    def test_sort_letters_some_appear_multiple(self):
        # arrange
        text = "tree"

        # act
        result = sort_letters(text)

        # assert
        self.assertEqual("eetr", result)

    def test_all_appear_multiple(self):
        # arrange
        text = "cccaaa"

        # act
        result = sort_letters(text)

        # assert
        self.assertEqual("cccaaa", result)

    def test_handles_capitals(self):
        # arrrange
        text = "HHeEgg"

        # act
        result = sort_letters(text)

        # assert
        self.assertEqual("HHggeE", result)
