import unittest
from thirty_day_challenge.day_29 import get_max_path_sum, create_tree_from_list


class TestDay29(unittest.TestCase):

    def test_get_max_path_sum(self):
        # arrange
        tree = create_tree_from_list([-2])

        # act
        result = get_max_path_sum(tree)

        # assert
        self.assertEqual(-2, result)

    def test_get_max_path_sum_path_to_root_is_max(self):
        # arrange
        tree = create_tree_from_list([1, 2, -1])

        # act
        result = get_max_path_sum(tree)

        # assert
        self.assertEqual(3, result)

    def test_get_max_path_sum_max_not_through_root(self):
        # arrange
        tree = create_tree_from_list([-10, 9, 20, None, None, 15, 7])

        # act
        result = get_max_path_sum(tree)

        # assert
        self.assertEqual(42, result)

    def test_get_max_path_sum__max_through_root(self):
        # arrange
        tree = create_tree_from_list([3, 4, 1, 8, None, 5, 7, 2, None, None, None, None, None])

        # act
        result = get_max_path_sum(tree)

        # assert
        self.assertEqual(25, result)
