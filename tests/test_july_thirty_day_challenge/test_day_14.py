import unittest
from july_thirty_day_challenge.day_14 import get_angle


class TestDay14(unittest.TestCase):

    def test_zero_angle(self):
        # arrange
        hours = 12
        minutes = 0

        # act
        result = get_angle(hours, minutes)

        # assert
        self.assertEqual(0, result)

    def test_hour_hand_first(self):
        # arrange
        hours = 3
        minutes = 30

        # act
        result = get_angle(hours, minutes)

        # assert
        self.assertEqual(75, result)

    def test_minute_hand_first(self):
        # arrange
        hours = 3
        minutes = 15

        # act
        result = get_angle(hours, minutes)

        # assert
        self.assertEqual(7.5, result)

    def test_get_smaller_angle(self):
        # arrange
        hours = 1
        minutes = 57

        # act
        result = get_angle(hours, minutes)

        # assert
        self.assertEqual(76.5, result)