import unittest
from july_thirty_day_challenge.day_22 import get_zig_zag, create_tree_from_list


class TestDay22(unittest.TestCase):

    def test_no_root(self):
        # arrange
        root = None

        # act
        result = get_zig_zag(root)

        # assert
        self.assertSequenceEqual([], result)

    def test_complete(self):
        # arrange
        root = create_tree_from_list([1, 2, 3, 4, 5, 6, 7])

        # act
        result = get_zig_zag(root)

        # assert
        self.assertSequenceEqual([[1], [3, 2], [4, 5, 6, 7, 8]], result)

    def test_incomplete(self):
        # arrange
        root = create_tree_from_list([1, 2, 3, 4, None, None, 5])

        # act
        result = get_zig_zag(root)

        # assert
        self.assertSequenceEqual([[1], [3, 2], [4, 5]], result)

    def test_straight_line(self):
        # arrange
        root = create_tree_from_list([1, None, 2, None, 3, 4])

        # act
        result = get_zig_zag(root)

        # assert
        self.assertSequenceEqual([[1], [2], [3], [4]], result)