import unittest
from thirty_day_challenge.day_4 import all_zeroes_at_end_v1, all_zeroes_at_end_v2


class TestDay4(unittest.TestCase):

    def test_all_zeroes_at_end_no_zeroes(self):
        # arrange
        arr = [1, 2, 3, 4]

        # act
        all_zeroes_at_end_v2(arr)

        # assert
        self.assertSequenceEqual([1, 2, 3, 4], arr)

    def test_all_zeroes_at_end_all_zeroes(self):
        # arrange
        arr = [0, 0, 0, 0, 0]

        # act
        all_zeroes_at_end_v2(arr)

        # assert
        self.assertSequenceEqual([0, 0, 0, 0, 0], arr)

    def test_all_zeroes_at_end_zeroes_at_start(self):
        # arrange
        arr = [0, 0, 1, 2, -4, 5]

        # act
        all_zeroes_at_end_v2(arr)

        # assert
        self.assertSequenceEqual([1, 2, -4, 5, 0, 0], arr)

    def test_all_zeroes_at_end_zeroes_in_middle(self):
        # arrange
        arr = [1, 2, 0, 3, 0, 4, 4, 0, 5]

        # act
        all_zeroes_at_end_v2(arr)

        # assert
        self.assertSequenceEqual([1, 2, 3, 4, 4, 5, 0, 0, 0], arr)

    def test_all_zeroes_at_end_zeroes_start_and_end(self):
        # arrange
        arr = [0, 1, 2, 0, 3, 4, 0, 0]

        # act
        all_zeroes_at_end_v2(arr)

        # assert
        self.assertSequenceEqual([1, 2, 3, 4, 0, 0, 0, 0], arr)
