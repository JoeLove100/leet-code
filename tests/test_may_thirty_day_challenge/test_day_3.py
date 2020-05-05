import unittest
from may_thirty_day_challenge.day_3 import can_construct


class TestDay3(unittest.TestCase):

    def test_can_construct_no_available_letters(self):
        # arrange
        target = "a"
        available_letters = ""

        # act
        result = can_construct(target, available_letters)

        # assert
        self.assertFalse(result)

    def test_can_construct_no_target(self):
        # arrange
        target = ""
        available_letters = "bd"

        # act
        result = can_construct(target, available_letters)

        # assert
        self.assertTrue(result)

    def test_can_construct_different_letters(self):
        # arrange
        target = "abcd"
        available_letters = "abce"

        # act
        result = can_construct(target, available_letters)

        # assert
        self.assertFalse(result)

    def test_can_construct_missing_letters(self):
        # arrange
        target = "abdc"
        available_letters = "acd"

        # act
        result = can_construct(target, available_letters)

        # assert
        self.assertFalse(result)

    def test_can_construct_not_enough_letters(self):
        # arrange
        target = "aaabbbcc"
        available_letters = "aaabbcc"

        # act
        result = can_construct(target, available_letters)

        # assert
        self.assertFalse(result)

    def test_can_construct(self):
        # arrange
        target = "aaabbbcc"
        available_letters = "abcabcab"

        # act
        result = can_construct(target, available_letters)

        # assert
        self.assertTrue(result)
