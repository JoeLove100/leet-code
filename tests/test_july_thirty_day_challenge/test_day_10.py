import unittest
from july_thirty_day_challenge.day_10 import get_flattened_list

# did most of the testing on leetcode as setting up the lists is a pain


class TestDay10(unittest.TestCase):

    def test_null_root(self):
        # arrange
        root = None

        # act
        result = get_flattened_list(root)

        # assert
        self.assertIsNone(result)
