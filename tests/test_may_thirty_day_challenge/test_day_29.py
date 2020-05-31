import unittest
from may_thirty_day_challenge.day_29 import is_possible


class TestDay29(unittest.TestCase):

    def test_no_prereq(self):
        # arrange
        n = 10
        prereq = []

        # act
        result = is_possible(prereq, n)

        # assert
        self.assertTrue(result)

    def test_only_one_prereq(self):
        # arrange
        n = 4
        prereq = [[1, 2]]

        # act
        result = is_possible(prereq, n)

        # assert
        self.assertTrue(result)

    def test_loop_exists(self):
        # arrange
        n = 4
        prereq = [[2, 3], [3, 1], [1, 2]]

        # act
        result = is_possible(prereq, n)

        # assert
        self.assertFalse(result)
