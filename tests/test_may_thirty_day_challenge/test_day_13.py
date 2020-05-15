import unittest
from may_thirty_day_challenge.day_13 import get_smallest_number


class TestDay13(unittest.TestCase):

    def test_get_smallest_number_k_is_zero(self):
        # arrange
        n = 123
        k = 0

        # act
        result = get_smallest_number(n, k)

        # assert
        self.assertEqual(123, result)

    def test_get_smallest_number_single_digit(self):
        # arrange
        n = 5
        k = 1

        # act
        result = get_smallest_number(n, k)

        # act
        self.assertEqual(0, result)

    def test_get_smallest_number_remove_all_digits(self):
        # arrange
        n = 1234
        k = 4

        # act
        result = get_smallest_number(n, k)

        # act
        self.assertEqual(0, result)

    def test_get_smallest_number_remove_multiple(self):
        # arrange
        n = 1432219
        k = 3

        # act
        result = get_smallest_number(n, k)

        # assert
        self.assertEqual(1219, result)

    def test_get_smallest_number_handle_zeros(self):
        # arrange
        n = 100200
        k = 1

        # act
        result = get_smallest_number(n, k)

        # assert
        self.assertEqual(200, result)

    def test_get_smallest_number_remove_at_end(self):
        # arrange
        n = 1112
        k = 2

        # act
        result = get_smallest_number(n, k)

        # assert
        self.assertEqual(11, result)

    def test_get_smallest_number_in_order(self):
        # arrange
        n = 12345
        k = 2

        # act
        result = get_smallest_number(n, k)

        # assert
        self.assertEqual(123, result)

    def test_get_smallest_number_all_same(self):
        # arrange
        n = 444444
        k = 4

        # act
        result = get_smallest_number(n, k)

        # assert
        self.assertEqual(44, result)

    def test_remove_all_in_first_step(self):
        # arrange
        n = 543221
        k = 4

        # act
        result = get_smallest_number(n, k)

        # assert
        self.assertEqual(21, result)

    def test_get_smallest_number_only_zeroes_left(self):
        # arrange
        n = 505000
        k = 2

        # act
        result = get_smallest_number(n, k)

        # assert
        self.assertEqual(0, result)
