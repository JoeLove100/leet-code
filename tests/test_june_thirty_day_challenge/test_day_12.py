import unittest
import random
from june_thirty_day_challenge.day_12 import RandomizedSet


class TestDay12(unittest.TestCase):

    def test_insert_not_in_set(self):
        # arrange
        rs = RandomizedSet()
        rs.insert(3)
        rs.insert(5)

        # act
        result = rs.insert(2)

        # assert
        self.assertTrue(result)

    def test_insert_in_set(self):
        # arrange
        rs = RandomizedSet()
        rs.insert(3)
        rs.insert(5)

        # act
        result = rs.insert(3)

        # assert
        self.assertFalse(result)

    def test_remove_not_in_set(self):
        # arrange
        rs = RandomizedSet()
        rs.insert(3)
        rs.insert(1)
        rs.insert(8)

        # act
        result = rs.remove(4)

        # assert
        self.assertFalse(result)

    def test_remove_in_set_at_end(self):
        # arrange
        rs = RandomizedSet()
        rs.insert(3)
        rs.insert(1)
        rs.insert(8)

        # act
        result = rs.remove(8)

        # assert
        self.assertTrue(result)

    def test_remove_in_set_before_end(self):
        # arrange
        rs = RandomizedSet()
        rs.insert(3)
        rs.insert(1)
        rs.insert(8)

        # act
        result = rs.remove(1)

        # assert
        self.assertTrue(result)

    def test_get_random(self):
        # arrange
        rs = RandomizedSet()
        rs.insert(2)
        rs.insert(3)
        random.seed(1234)

        # act
        result = rs.getRandom()

        # assert
        self.assertEqual(3, result)

