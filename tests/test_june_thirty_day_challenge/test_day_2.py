import unittest
from june_thirty_day_challenge.day_2 import get_nth_node, linked_list_to_array, array_to_linked_list, \
    remove_node


class TestDay2(unittest.TestCase):

    def test_only_three_nodes(self):
        # arrange
        linked_list = array_to_linked_list([1, 2, 3])
        to_remove = get_nth_node(linked_list, 1)

        # act
        remove_node(to_remove)
        result = linked_list_to_array(linked_list)

        # assert
        self.assertSequenceEqual([1, 3], result)

    def test_several_nodes(self):
        # arrange
        linked_list = array_to_linked_list([1, 2, 3, 7, 8, 6, 5, 4])
        to_remove = get_nth_node(linked_list, 2)

        # act
        remove_node(to_remove)
        result = linked_list_to_array(linked_list)

        # assert
        self.assertSequenceEqual([1, 2, 7, 8, 6, 5, 4], result)
