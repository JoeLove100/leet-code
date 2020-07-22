import unittest
from july_thirty_day_challenge.day_19 import create_linked_list, create_array, remove_val


class TestDay19(unittest.TestCase):

    def test_no_node(self):
        # arrange
        head = None
        val = 2

        # act
        result = remove_val(head, val)

        # assert
        self.assertIsNone(result)

    def test_no_nodes_to_remove(self):
        # arrange
        head = create_linked_list([1, 2, 5, -3, 2, 10])
        val = 4

        # act
        result = remove_val(head, val)
        result_as_array = create_array(result)

        # assert
        self.assertSequenceEqual([1, 2, 5, -3, 2, 10], result_as_array)

    def test_remove_middle_node(self):
        # arrange
        head = create_linked_list([1, 2, 5, 2, 3, 2, 2, 1])
        val = 2

        # act
        result = remove_val(head, val)
        result_as_array = create_array(result)

        # assert
        self.assertSequenceEqual([1, 5, 3, 1], result_as_array)

    def test_remove_end_nodes(self):
        # arrange
        head = create_linked_list([1, 2, 3, -1, -1, -1])
        val = -1

        # act
        result = remove_val(head, val)
        result_as_array = create_array(result)

        # assert
        self.assertSequenceEqual([1, 2, 3], result_as_array)

    def test_remove_start_nodes(self):
        # arrange
        head = create_linked_list([5, 5, 6, 9, 7])
        val = 5

        # act
        result = remove_val(head, val)
        result_as_array = create_array(result)

        # assert
        self.assertSequenceEqual([6, 9, 7], result_as_array)

    def test_remove_all_nodes(self):
        # arrange
        head = create_linked_list([0, 0, 0, 0, 0])
        val = 0

        # act
        result = remove_val(head, val)

        # assert
        self.assertIsNone(result)
