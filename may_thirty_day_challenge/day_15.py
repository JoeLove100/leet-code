"""
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.
(Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.
"""

from typing import List
from collections import deque


def get_max_subarray(arr: List[int]) -> int:
    return get_max_circular_sub_array_3(arr)


def get_max_circular_sub_array_1(arr: List[int]) -> int:

    # first, us Kandane algo to get max for non-circular arrays
    dp = arr[0]
    max_circular_sum = dp
    for n in arr[1:]:
        dp = n + max(dp, 0)
        max_circular_sum = max(max_circular_sum, dp)

    # then get all right sums
    right_sums = [0 for _ in range(len(arr))]
    right_sums[-1] = arr[-1]
    for i in range(len(arr) - 2, -1, -1):
        right_sums[i] = right_sums[i + 1] + arr[i]

    # now get the MAX right sum at each position
    max_right_sums = [0 for _ in range(len(arr))]
    max_right_sums[-1] = max(right_sums[-1], 0)
    for i in range(len(arr) - 2, -1, -1):
        max_right_sums[i] = max(max_right_sums[i + 1], right_sums[i])

    # finally, get answer as max of Kadane one period and left sum + optimal right sum
    left_sum = 0
    for i in range(len(arr) - 1):
        left_sum += arr[i]
        max_circular_sum = max(max_circular_sum, left_sum + max_right_sums[i + 1])

    return max_circular_sum


def get_max_circular_sub_array_2(arr: List[int]) -> int:

    # double the array size, and get a list of left sums
    arr_length = len(arr)
    arr.extend(arr)
    left_sums = [0 for _ in range(len(arr))]
    left_sums[0] = arr[0]
    for i, n in enumerate(arr[1:]):
        left_sums[i + 1] = left_sums[i] + n

    # for each j in range(len(arr)), find the i such that
    # left_sums[i] is as small as possible and j - i <= arr_length

    circular_max = arr[0]
    q = deque([0])

    for j in range(1, len(arr[1:])):

        if q[0] < j - arr_length:  # remove i if i is too small
            q.popleft()

        circular_max = max(circular_max, left_sums[j] - left_sums[q[0]])

        while q and left_sums[j] <= left_sums[q[-1]]:  # only keep entries in q better than j
            q.pop()

        q.append(j)

    return circular_max


def get_max_circular_sub_array_3(arr: List[int]) -> int:

    # first define an implementation of Kadane to get the min
    # subarray sum rather than than the max

    if len(arr) == 1:
        return arr[0]

    def min_kadane(subarray):

        current_min = subarray[0]
        min_sum = current_min
        for i in range(1, len(subarray)):
            current_min = subarray[i] + min(0, current_min)
            min_sum = min(current_min, min_sum)

        return min_sum

    full_arr_sum = sum(arr)
    min_shifted_1 = min_kadane(arr[1:])
    min_shifted_2 = min_kadane(arr[:-1])

    max_two_array = full_arr_sum - min(min_shifted_2, min_shifted_1)
    max_one_array = -min_kadane([-n for n in arr])
    return max(max_two_array, max_one_array)
