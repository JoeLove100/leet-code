"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version
of your product fails the quality check. Since each version is developed based on the previous version, all the
versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes
all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to
find the first bad version. You should minimize the number of calls to the API.
"""
from typing import List, Callable
import math


def get_is_bad_version(arr: List[bool]) -> Callable[[int], bool]:

    def partial(i: int):
        return arr[i]

    return partial


def _is_bad_version(start: int,
                    end: int,
                    is_bad_version: Callable[[int], bool]) -> int:

    if end - start <= 1:
        return end

    mid = math.floor((start + end) / 2)
    mid_version = is_bad_version(mid)
    previous_version = is_bad_version(mid - 1)

    if not mid_version and previous_version:
        return mid_version + 1
    elif not mid_version:
        return _is_bad_version(start, mid, is_bad_version)
    else:
        return _is_bad_version(mid + 1, end, is_bad_version)


def get_first_bad_version(n: int,
                          is_bad_version: Callable[[int], bool]) -> int:

    return _is_bad_version(0, n, is_bad_version)





