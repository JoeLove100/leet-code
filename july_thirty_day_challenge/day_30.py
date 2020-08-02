"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct
a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

-> The same word in the dictionary may be reused multiple times in the segmentation.
-> You may assume the dictionary does not contain duplicate words.
"""

from typing import List, Set, Dict


def _get_words(s: str,
               pos: int,
               word_dict: Set[str],
               memo: Dict[int, List[str]]) -> List[str]:

    all_words = []
    for i in range(pos + 1, len(s) + 1):
        if s[pos:i] in word_dict:

            if i == len(s):
                all_words.append(s[pos:i])
            else:
                if i in memo:
                    words = memo[i]
                else:
                    words = _get_words(s, i, word_dict, memo)
                    memo[i] = words

                all_words.extend([s[pos:i] + " " + w for w in words])

    return all_words


def get_all_words(s: str,
                  word_dict: List[str]) -> List[str]:

    if not s or not word_dict:
        return []

    all_words = _get_words(s, 0, set(word_dict), dict())
    return all_words


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return get_all_words(s, wordDict)
