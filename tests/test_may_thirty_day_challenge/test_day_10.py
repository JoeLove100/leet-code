import unittest
from may_thirty_day_challenge.day_10 import find_town_judge


class TestDay10(unittest.TestCase):

    def test_find_judge_two_people_judge_exists(self):
        # arrange
        n = 2
        trust = [[1, 2]]

        # act
        result = find_town_judge(n, trust)

        # assert
        self.assertEqual(2, result)

    def test_find_judge_no_judge(self):
        # arrange
        n = 3
        trust = [[1, 3], [2, 3], [3, 1]]

        # act
        result = find_town_judge(n, trust)

        # assert
        self.assertEqual(-1, result)

    def test_find_judge_judge_exists(self):
        # arrange
        n = 4
        trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]

        # act
        result = find_town_judge(n, trust)

        # arrange
        self.assertEqual(3, result)
