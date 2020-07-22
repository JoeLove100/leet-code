import unittest
from july_thirty_day_challenge.day_18 import get_course_order


class TestDay18(unittest.TestCase):

    def test_no_edges(self):
        # arrange
        arr = []

        # act
        result = get_course_order(arr, 0)

        # assert
        self.assertEqual([], result)

    def test_one_edge(self):
        # arrange
        arr = [[1, 0]]

        # act
        result = get_course_order(arr, 2)

        # assert
        self.assertEqual([0, 1], result)

    def test_no_dependencies(self):
        # arrange
        arr = []

        # act
        result = get_course_order(arr, 4)

        # act
        self.assertSequenceEqual([3, 2, 1, 0], result)

    def test_multiple_connected_parts(self):
        # arrange
        arr = [[0, 5], [1, 0], [2, 1]]

        # act
        result = get_course_order(arr, 6)

        # assert
        self.assertSequenceEqual([5, 4, 3, 0, 1, 2], result)

    def test_multiple_solutions(self):
        # arrange
        arr = [[1, 0], [2, 0], [3, 1], [3, 2]]

        # act
        result = get_course_order(arr, 4)

        # assert
        self.assertSequenceEqual([0, 2, 1, 3], result)

    def test_not_dag(self):
        # arrange
        arr = [[0, 1], [1, 0]]

        # act
        result = get_course_order(arr, 2)

        # assert
        self.assertSequenceEqual([], result)
