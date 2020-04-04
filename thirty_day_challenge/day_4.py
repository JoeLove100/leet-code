from typing import List


def swap(arr: List[int],
         i: int,
         j: int) -> None:

    arr[i], arr[j] = arr[j], arr[i]


def all_zeroes_at_end_v1(arr: List[int]) -> None:
    """
    move all zero elements to the end
    of arr in place
    """

    zero_count = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            zero_count += 1
        else:
            for j in range(zero_count):
                swap(arr, i - j, i - (j + 1))


def all_zeroes_at_end_v2(arr: List[int]) -> None:
    """
    move all zero elements to the end
    of arr in place
    """

    correct_positions = dict()
    zero_count = 0

    for i, n in enumerate(arr):
        if n != 0:
            correct_positions.update({i - zero_count: n})
        else:
            zero_count += 1
            correct_positions.update({len(arr) - zero_count: n})

    for i in range(len(arr)):
        arr[i] = correct_positions[i]


def moveZeroes(nums: List[int]) -> None:
    n = len(nums)
    place = 0
    i = 0
    while i < n:
        if nums[i] != 0:
            if place != i:
                nums[place], nums[i] = nums[i], 0
                place += 1
        i += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        all_zeroes_at_end_v2(nums)


if __name__ == "__main__":

    import random
    random.seed(1234)
    import cProfile

    arr = [random.randint(-50, 50) for _ in range(int(1e6))]
    cProfile.run(f"all_zeroes_at_end_v2({arr})")
