import unittest
from june_thirty_day_challenge.day_21 import get_min_health_points


class TestDay21(unittest.TestCase):

    def test_no_dungeon(self):
        # arrange
        dungeon_1 = []
        dungeon_2 = [[]]

        # act
        result_1 = get_min_health_points(dungeon_1)
        result_2 = get_min_health_points(dungeon_2)

        # assert
        self.assertEqual(1, result_1)
        self.assertEqual(1, result_2)

    def test_one_cell_dungeon_neg(self):
        # arrange
        dungeon = [[-3]]

        # act
        result = get_min_health_points(dungeon)

        # assert
        self.assertEqual(4, result)

    def test_one_cell_positive(self):
        # arrange
        dungeon = [[6]]

        # act
        result = get_min_health_points(dungeon)

        # assert
        self.assertEqual(1, result)

    def test_actual_dungeon(self):
        # arrange
        dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]

        # act
        result = get_min_health_points(dungeon)

        # assert
        self.assertEqual(7, result)

    def test_row(self):
        # arrange
        dungeon = [[0, 0]]

        # act
        result = get_min_health_points(dungeon)

        # assert
        self.assertEqual(1, result)

    def test_column(self):
        # arrange
        dungeon = [[-2], [-3], [-2]]

        # act
        result = get_min_health_points(dungeon)

        # assert
        self.assertEqual(8, result)
