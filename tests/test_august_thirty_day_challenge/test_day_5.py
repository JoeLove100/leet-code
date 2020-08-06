import unittest
from august_thirty_day_challenge.day_5 import WordDictionary


class TestDay5(unittest.TestCase):

    def test_word_in_dict(self):
        # arrange
        wd = WordDictionary()
        wd.addWord("cat")
        wd.addWord("cot")
        wd.addWord("candle")

        # assert
        result = wd.search("cot")

        # assert
        self.assertTrue(result)

    def test_word_not_in_dict(self):
        # arrange
        wd = WordDictionary()
        wd.addWord("cat")
        wd.addWord("cot")
        wd.addWord("candle")

        # act
        result = wd.search("car")

        # assert
        self.assertFalse(result)

    def test_word_too_long(self):
        # arrange
        wd = WordDictionary()
        wd.addWord("cast")

        # act
        result = wd.search("caster")

        # assert
        self.assertFalse(result)

    def test_handles_dot_at_start(self):
        # arrange
        wd = WordDictionary()
        wd.addWord("bat")
        wd.addWord("cat")
        wd.addWord("best")

        # act
        result = wd.search(".at")

        # assert
        self.assertTrue(result)

    def test_handle_dot_in_middle(self):
        # arrange
        wd = WordDictionary()
        wd.addWord("deed")
        wd.addWord("dad")
        wd.addWord("deer")

        # act
        result = wd.search("d..d")

        # assert
        self.assertTrue(result)

    def test_handle_dot_at_end(self):
        # arrange
        wd = WordDictionary()
        wd.addWord("test")
        wd.addWord("tent")

        # arrange
        result = wd.search("t.s.")

        # act
        self.assertTrue(result)

    def test_dot_at_end_too_long(self):
        # arrange
        wd = WordDictionary()
        wd.addWord("ca")
        wd.addWord("co")
        wd.addWord("ba")

        # act
        result = wd.search(".a.")

        # assert
        self.assertFalse(result)

    def test_contains_superstring(self):
        # arrange
        wd = WordDictionary()
        wd.addWord("testing")

        # act
        result = wd.search("t.s.")

        # assert
        self.assertFalse(result)


