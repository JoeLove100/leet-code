import unittest
from thirty_day_challenge.day_9 import are_same, get_next_char_index


class TestDay9(unittest.TestCase):

    def test_are_same_empty(self):
        # arrange
        s_1 = ""
        s_2 = ""

        # act
        result = are_same(s_1, s_2)

        # assert
        self.assertTrue(result)

    def test_are_same_backspace_only(self):
        # arrange
        s_1 = "##"
        s_2 = "#####"

        # act
        result = are_same(s_1, s_2)

        # assert
        self.assertTrue(result)

    def test_are_same_both_ultimately_empty(self):
        # arrange
        s_1 = "ab##"
        s_2 = "a#b#c#d#e#"

        # act
        result = are_same(s_1, s_2)

        # assert
        self.assertTrue(result)

    def test_are_same_same_should_be_false(self):
        # arrange
        s_1 = "bb#c"
        s_2 = "ab#c"

        # act
        result = are_same(s_1, s_2)

        # assert
        self.assertFalse(result)

    def test_are_same_should_be_true(self):
        # arrange
        s_1 = "a##c"
        s_2 = "#a#c"

        # act
        result = are_same(s_1, s_2)

        # assert
        self.assertTrue(result)

    def test_get_next_char_index_empty(self):
        # arrange
        text = ""

        # act
        result = get_next_char_index(text, -1)

        # assert
        self.assertEqual(-1, result)

    def test_get_next_char_index_not_hash(self):
        # arrange
        text = "abcde"

        # act
        result = get_next_char_index(text, 3)

        # assert
        self.assertEqual(3, result)

    def test_get_next_char_consecutive_hashes(self):
        # arrange
        text = "abcd###a"

        # act
        result = get_next_char_index(text, 6)

        # assert
        self.assertEqual(0, result)

    def test_get_next_char_intermittent_hashes(self):
        # arrange
        text = "#abc#d##"

        # act
        result = get_next_char_index(text, 7)

        # assert
        self.assertEqual(1, result)

    def test_get_next_char_alternating_hashes(self):
        # arrange
        text = "a##b#c#d#e#"

        # act
        result = get_next_char_index(text, 10)

        # assert
        self.assertEqual(-1, result)
