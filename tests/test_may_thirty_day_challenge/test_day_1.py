import unittest
from may_thirty_day_challenge.day_1 import  get_first_bad_version, get_is_bad_version


class TestDay1(unittest.TestCase):

    def test_get_first_bad_version_one_version(self):
        # arrange
        func = get_is_bad_version([False])

        # act
        result = get_first_bad_version(1, func)

        # assert
        self.assertEqual(1, result)

    def test_get_first_bad_version_in_first_half(self):
        # arrange
        func = get_is_bad_version([True, False, False, False, False])

        # act
        result = get_first_bad_version(5, func)

        # assert
        self.assertEqual(1, result)

    def test_get_first_bad_version_in_second_half(self):
        # arrange
        func = get_is_bad_version([True, True, True, True, True, False, False, False])

        # act
        result = get_first_bad_version(8, func)

        # assert
        self.assertEqual(6, result)

    def test_get_first_bad_version_last_version(self):
        # arrange
        func = get_is_bad_version([True, True, True, False])

        # act
        result = get_first_bad_version(4, func)

        # assert
        self.assertEqual(4, result)
