import unittest
from june_thirty_day_challenge.day_4 import reverse_string


class TestDay4(unittest.TestCase):

    def test_no_string(self):
        # arrange
        text = []

        # act
        reverse_string(text)

        # assert
        self.assertSequenceEqual([], text)

    def test_odd_number_characters(self):
        # arrange
        text = list("heron")

        # act
        reverse_string(text)

        # assert
        self.assertSequenceEqual(list("noreh"), text)

    def test_even_number_characters(self):
        # arrange
        text = list("hermit")

        # act
        reverse_string(text)

        # assert
        self.assertSequenceEqual(list("timreh"), text)
