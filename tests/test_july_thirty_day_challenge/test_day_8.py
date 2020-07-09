import unittest
from july_thirty_day_challenge.day_8 import get_triples


class TestDay8(unittest.TestCase):

    def test_length_two(self):
        # arrange
        arr = [1, 2]

        # act
        result = get_triples(arr)

        # assert
        self.assertSequenceEqual([], result)

    def test_all_zeroes(self):
        # arrange
        arr = [0, 0, 0, 0, 0]

        # act
        result = get_triples(arr)

        # assert
        self.assertSequenceEqual([[0, 0, 0]], result)

    def test_repeated_triple(self):
        # arrange
        arr = [1, 1, -2, -2, 1, 1]

        # act
        result = get_triples(arr)

        # assert
        self.assertSequenceEqual([[-2, 1, 1]], result)

    def test_doubled_element(self):
        # arrange
        arr = [-2, 1, 4, 1]

        # act
        result = get_triples(arr)

        # assert
        self.assertSequenceEqual([[-2, 1, 1]], result)

    def test_repeated_element_required(self):
        # arrange
        arr = [10, 20, -6, 3, 1, 0, 0]

        # act
        result = get_triples(arr)

        # assert
        self.assertSequenceEqual([], result)