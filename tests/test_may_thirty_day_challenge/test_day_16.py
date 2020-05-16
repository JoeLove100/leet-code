import unittest
from may_thirty_day_challenge.day_16 import list_to_linked_list, linked_list_to_list, sort_by_parity


class TestDay16(unittest.TestCase):

    def test_two_nodes_only(self):
        # arrange
        root = list_to_linked_list([1, 5])

        # act
        sort_by_parity(root)
        result = linked_list_to_list(root)

        # assert
        expected_result = [1, 5]
        self.assertSequenceEqual(expected_result, result)

    def test_three_nodes_only(self):
        # arrange
        root = list_to_linked_list(([1, 2, 3]))

        # act
        sort_by_parity(root)
        result = linked_list_to_list(root)

        # assert
        expected_result = [1, 3, 2]
        self.assertSequenceEqual(expected_result, result)

    def test_odd_number_of_nodes(self):
        # arrange
        root = list_to_linked_list([1, 2, 3, 4, 5])

        # act
        sort_by_parity(root)
        result = linked_list_to_list(root)

        # assert
        expected_result = [1, 3, 5, 2, 4]
        self.assertSequenceEqual(expected_result, result)

    def test_even_number_of_nodes(self):
        # arrange
        root = list_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        # act
        sort_by_parity(root)
        result = linked_list_to_list(root)

        # assert
        expected_result = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
        self.assertSequenceEqual(expected_result, result)
