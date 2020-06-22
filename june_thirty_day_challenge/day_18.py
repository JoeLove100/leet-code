"""
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more
times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated
substring, the answer is "".)
"""
from typing import Generator


def rolling_hash(text: str,
                 k: int,
                 a: int) -> Generator[int, None, None]:

    initial_hash = 0

    for i, c in enumerate(text[:k]):
        initial_hash += ord(c) * a ** (k - 1 - i)

    yield initial_hash

    current_hash = initial_hash
    for i, c in enumerate(text[k:]):
        current_hash -= ord(text[i]) * a ** (k - 1)
        current_hash *= a
        current_hash += ord(text[i + k])
        yield current_hash


def _get_length_k_solution(text: str,
                           k: int) -> str:

    prev_hashes = set()
    gen = rolling_hash(text, k, 26)

    for i in range(len(text) - k + 1):
        rolled_hash = next(gen)
        if rolled_hash in prev_hashes:
            if text[i: i + k] in text[:i + k - 1]:
                return text[i: i + k]
        else:
            prev_hashes.add(rolled_hash)

    return ""


def get_longest_duped_string(text: str) -> str:

    if not text:
        return text

    lo, hi = 0, len(text)
    max_substring = ""

    while True:

        mid = (hi + lo) // 2
        substring = _get_length_k_solution(text, mid)
        if not substring:
            hi = mid
        else:
            max_substring = substring
            lo = mid + 1

        if hi == lo:
            return max_substring


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        return get_longest_duped_string(S)


if __name__ == "__main__":

    # import string
    import random
    import cProfile

    random.seed(1234)
    text = "".join([random.choice(["a", "b"]) for _ in range(10000)])

    cProfile.run(f"get_longest_duped_string('{text}')")
