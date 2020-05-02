import unittest
from april_thirty_day_challenge.day_28 import FirstUnique


class TestDay28(unittest.TestCase):

    def test_first_unique_no_items(self):
        # arrange
        first_unique = FirstUnique([])

        # act
        result = first_unique.showFirstUnique()

        # assert
        self.assertEqual(-1, result)

    def test_first_unique_handles_duplicates(self):
        # arrange
        first_unique = FirstUnique([1, 2, 4, 3, 2, 3, 1])

        # act
        result = first_unique.showFirstUnique()

        # assert
        self.assertEqual(4, result)

    def test_first_unique_handles_additions(self):
        # arrange
        first_unique = FirstUnique([1, 2, 3, 2])
        first_unique.add(1)
        first_unique.add(2)

        # act
        result = first_unique.showFirstUnique()

        # assert
        self.assertEqual(3, result)

    def test_first_unique_multiple_shows(self):
        # arrange
        first_unique = FirstUnique([2, 3, 3, 4, 4, 1])
        first_unique.showFirstUnique()
        first_unique.showFirstUnique()
        first_unique.showFirstUnique()

        # act
        result = first_unique.showFirstUnique()

        # assert
        self.assertEqual(2, result)

