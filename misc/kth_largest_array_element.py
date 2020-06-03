"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
not the kth distinct element.
"""
import math
from typing import List


def _get_largest_k_combined(arr_1: List[int],
                            arr_2: List[int],
                            k: int) -> List[int]:

    arr_merged = []
    i = j = 0
    while i < len(arr_1) and j < len(arr_2) and (i + j) < k:
        if arr_1[i] > arr_2[j]:
            arr_merged.append(arr_1[i])
            i += 1
        else:
            arr_merged.append(arr_2[j])
            j += 1

    if i == len(arr_1) and i + j < k:
        arr_merged.extend(arr_2[j: k - i])
    elif j == len(arr_2) and i + j < k:
        arr_merged.extend(arr_1[i: k - j])

    return arr_merged


def _get_largest_k(arr: List[int],
                   low: int,
                   high: int,
                   k: int) -> List[int]:

    if low == high - 1:
        return arr[low: high]

    mid = math.floor((low + high) / 2)
    largest_k_low = _get_largest_k(arr, low, mid, k)
    largest_k_high = _get_largest_k(arr, mid, high, k)
    return _get_largest_k_combined(largest_k_low, largest_k_high, k)


def get_kth_largest_element(arr: List[int],
                            k: int) -> int:
    largest_k = _get_largest_k(arr, 0, len(arr), k)
    return largest_k[-1]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return get_kth_largest_element(nums, k)


if __name__ == "__main__":

    print(get_kth_largest_element([1, 2, 3, 4, 5, 6, 7], 6))

