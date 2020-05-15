import unittest
from may_thirty_day_challenge.day_14 import Trie


class TestDay14(unittest.TestCase):

    def test_can_add_words(self):
        # arrange
        trie = Trie()
        trie.insert("banana")
        trie.insert("bandana")

        # act
        result = trie.search("banana")

        # assert
        self.assertTrue(result)

    def test_returns_false_if_not_found(self):
        # arrange
        trie = Trie()
        trie.insert("banana")

        # act
        result = trie.search("banner")

        # assert
        self.assertFalse(result)

    def test_returns_false_search_suffix(self):
        # arrange
        trie = Trie()
        trie.insert("banana")

        # act
        result = trie.search("ban")

        # assert
        self.assertFalse(result)

    def test_returns_true_starts_with(self):
        # arrange
        trie = Trie()
        trie.insert("banana")

        # act
        result = trie.startsWith("ban")

        # assert
        self.assertTrue(result)

    def test_returns_true_starts_with_exact_match(self):
        # arrange
        trie = Trie()
        trie.insert("band")

        # act
        result = trie.startsWith("band")

        # assert
        self.assertTrue(result)

    def test_returns_false_starts_with_no_such_prefix(self):
        # arrange
        trie = Trie()
        trie.insert("banana")
        trie.insert("bandana")

        # act
        result = trie.startsWith("bad")

        # assert
        self.assertFalse(result)
