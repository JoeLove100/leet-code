import unittest
from thirty_day_challenge.day_8 import get_half_way_point, create_linked_list


class TestDay8(unittest.TestCase):

    def test_get_half_way_point_one_item(self):
        # arrange
        head = create_linked_list([1])

        # act
        result = get_half_way_point(head)

        # assert
        self.assertEqual(result.val, 1)

    def test_get_half_way_point_odd_items(self):
        # arrange
        head = create_linked_list([1, 2, 3, 4, 5])

        # act
        result = get_half_way_point(head)

        # assert
        self.assertEqual(result.val, 3)

    def test_get_half_way_point_even_items(self):
        # arrange
        head = create_linked_list([1, 2, 3, 4, 5, 6])

        # act
        result = get_half_way_point(head)

        # assert
        self.assertEqual(result.val, 4)
