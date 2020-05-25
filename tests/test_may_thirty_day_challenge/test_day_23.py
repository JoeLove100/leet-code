import unittest
from may_thirty_day_challenge.day_23 import get_intervals


class TestDay23(unittest.TestCase):

    def test_no_intervals(self):
        # act
        result_1 = get_intervals([[1, 3]], [])
        result_2 = get_intervals([], [[1, 3]])

        # assert
        self.assertSequenceEqual([], result_1)
        self.assertSequenceEqual([], result_2)

    def test_intervals_are_the_same(self):
        # act
        arr_1 = [[2, 4]]
        arr_2 = [[0, 1], [2, 4]]

        # act
        result = get_intervals(arr_1, arr_2)

        # assert
        self.assertSequenceEqual([[2, 4]], result)

    def test_single_number_overlap(self):
        # act
        arr_1 = [[0, 5], [8, 10]]
        arr_2 = [[5, 6], [7, 8]]

        # act
        result = get_intervals(arr_1, arr_2)

        # assert
        self.assertSequenceEqual([[5, 5], [8, 8]], result)

    def test_overlap_at_left_edge(self):
        # act
        arr_1 = [[3, 8]]
        arr_2 = [[1, 4], [10, 12], [20, 25]]

        # assert
        result_1 = get_intervals(arr_1, arr_2)
        result_2 = get_intervals(arr_2, arr_1)

        # assert
        self.assertSequenceEqual([[3, 4]], result_1)
        self.assertSequenceEqual([[3, 4]], result_2)

    def test_overlap_at_right_edge(self):
        # act
        arr_1 = [[2, 5]]
        arr_2 = [[3, 10]]

        # act
        result_1 = get_intervals(arr_1, arr_2)
        result_2 = get_intervals(arr_2, arr_1)

        # assert
        self.assertSequenceEqual(result_1, [[3, 5]])
        self.assertSequenceEqual(result_2, [[3, 5]])

    def test_sub_interval(self):
        # act
        arr_1 = [[1, 10]]
        arr_2 = [[2, 5], [7, 9]]

        # act
        result_1 = get_intervals(arr_1, arr_2)
        result_2 = get_intervals(arr_2, arr_1)

        # assert
        self.assertSequenceEqual([[2, 5], [7, 9]], result_1)
        self.assertSequenceEqual([[2, 5], [7, 9]], result_2)

    def test_multiple_overlaps(self):
        # act
        arr_1 = [[0, 2], [5, 10], [13, 23], [24, 25]]
        arr_2 = [[1, 5], [8, 12], [15, 24], [25, 26]]

        # act
        result = get_intervals(arr_1, arr_2)

        # assert
        expected_intervals = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
        self.assertSequenceEqual(expected_intervals, result)
