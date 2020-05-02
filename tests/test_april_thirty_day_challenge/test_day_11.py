import unittest
from april_thirty_day_challenge.day_11 import build_tree, get_max_path_length


class TestDay11(unittest.TestCase):

    def test_get_path_length_empty_input(self):
        # arrange
        arr = None

        # act
        result = get_max_path_length(arr)

        # assert
        self.assertEqual(0, result)

    def test_get_path_length_no_nodes(self):
        # arrange
        arr = build_tree([1])

        # act
        result = get_max_path_length(arr)

        # assert
        self.assertEqual(result, 0)

    def test_get_path_length_max_through_root(self):
        # arrange
        arr = build_tree([1, 2, 3, 4, 5, None, None, 6, 7, None, None, 8, 9])

        # act
        result = get_max_path_length(arr)

        # assert
        self.assertEqual(5, result)

    def test_get_path_length_max_not_through_root(self):
        # arrange
        arr = build_tree([1, 2, None, 3, 4, 5, 6, 7, 8])

        # act
        result = get_max_path_length(arr)

        # assert
        self.assertEqual(4, result)
