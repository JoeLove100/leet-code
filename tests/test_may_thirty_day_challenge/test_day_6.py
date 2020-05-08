import unittest
from may_thirty_day_challenge.day_6 import are_cousins, create_tree_from_list


class TestDay6(unittest.TestCase):

    def test_are_cousins_same_value(self):
        # arrange
        tree = create_tree_from_list([1, 2, 3, 4, None, 5, 6])

        # act
        result = are_cousins(tree, 2, 2)

        # assert
        self.assertFalse(result)

    def test_are_cousins_x_first(self):
        # arrange
        tree = create_tree_from_list([1, 2, None, 3, None, 4, 5])

        # act
        result = are_cousins(tree, 3, 5)

        # assert
        self.assertFalse(result)

    def test_are_cousins_y_first(self):
        # arrange
        tree = create_tree_from_list([1, 2, 3, 4, None, None, 5])

        # act
        result = are_cousins(tree, 5, 2)

        # assert
        self.assertFalse(result)

    def test_are_cousins_true(self):
        # arrange
        tree = create_tree_from_list([1, 2, 3, 4, None, 5, None, 6, 7, 8, 9])

        # act
        result = are_cousins(tree, 6, 9)

        # assert
        self.assertTrue(result)

    def test_are_cousins_same_parents(self):
        # arrange
        tree = create_tree_from_list([1, 2, 3])

        # act
        result = are_cousins(tree, 2, 3)

        # assert
        self.assertFalse(result)

