"""
Given an array of strings, group anagrams together. All inputs are lower case, and the order of
the output is not important.
"""

from typing import List
from collections import defaultdict


def get_anagram_groups(arr: List[str]) -> List[List[str]]:

    groups = dict()

    for text in arr:
        sorted_text = "".join(sorted(text))
        groups.setdefault(sorted_text, []).append(text)

    return list(groups.values())


def get_anagram_groups_def_dict(arr: List[str]) -> List[List[str]]:

    ans = defaultdict(list)
    for i in arr:
        ans[tuple(sorted(i))].append(i)

    return ans.values()


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return get_anagram_groups(strs)


if __name__ == "__main__":

    import random
    import string
    import cProfile
    random.seed(1234)

    words = []
    for _ in range(100000):
        wl = random.randint(3, 50)
        wrd = "".join([random.choice(string.ascii_lowercase) for _ in range(wl)])
        words.append(wrd)

    cProfile.run(f"get_anagram_groups({words})")
    cProfile.run(f"get_anagram_groups_def_dict({words})")
