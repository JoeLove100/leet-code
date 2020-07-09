import unittest
from july_thirty_day_challenge.day_9 import get_width, create_tree_from_list


class TestDay9(unittest.TestCase):

    def test_no_root(self):
        # arrange
        root = None

        # act
        result = get_width(root)

        # assert
        self.assertEqual(0, result)

    def test_one_node(self):
        # arrange
        root = create_tree_from_list([1])

        # act
        result = get_width(root)

        # assert
        self.assertEqual(1, result)

    def test_straight_line(self):
        # arrange
        root = create_tree_from_list([1, None, 2, None, 3, None, 4])

        # act
        result = get_width(root)

        # assert
        self.assertEqual(1, result)

    def test_complete_tree(self):
        # arrange
        root = create_tree_from_list([1, 2, 3, 4, 5, 6, 7])

        # act
        result = get_width(root)

        # assert
        self.assertEqual(4, result)

    def test_incomplete_tree(self):
        # arrange
        root = create_tree_from_list([1, 2, 3, None, 4, None, 5])

        # act
        result = get_width(root)

        # assert
        self.assertEqual(3, result)

    def test_widest_in_middle(self):
        # arrange
        root = create_tree_from_list([1, 2, 3, None, 4, None, None])

        # act
        result = get_width(root)

        # assert
        self.assertEqual(2, result)
