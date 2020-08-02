import unittest
from august_thirty_day_challenge.day_2 import MyHashSet


class TestDay2(unittest.TestCase):

    def test_add(self):
        # arrange
        hs = MyHashSet()

        # act
        hs.add(100)
        hs.add(1)
        hs.add(10001)

        # assert
        self.assertSequenceEqual([100], hs._map[100])
        self.assertSequenceEqual([1, 10001], hs._map[1])

    def test_remove(self):
        # arrange
        hs = MyHashSet()

        # act
        hs.add(100)
        hs.remove(100)

        # assert
        self.assertSequenceEqual([], hs._map[100])

    def test_contains(self):
        # arrange
        hs = MyHashSet()

        # act
        hs.add(100)
        hs.add(1)
        hs.add(10001)

        # assert
        self.assertTrue(hs.contains(10001))
        self.assertFalse(hs.contains(5))


