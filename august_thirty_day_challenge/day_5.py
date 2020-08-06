"""
Design a data structure that supports the following two operations:

-> void addWord(word)
-> bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it
can represent any one letter.
"""

from typing import List
from collections import deque


class Node:

    def __init__(self,
                 letter: str,
                 children: List["Node"]):

        self.letter = letter
        self.children = children


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self._tree = Node("", [])

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """

        word += "$"
        current = self._tree
        i = 0

        while i < len(word):

            matching_letter = False
            for node in current.children:
                if node.letter == word[i]:
                    current = node
                    i += 1
                    matching_letter = True
                    break

            if not matching_letter:
                break

        while i < len(word):
            next_node = Node(letter=word[i], children=[])
            current.children.append(next_node)
            current = next_node
            i += 1

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to
        represent any one letter.
        """

        word += "$"
        nodes = deque([self._tree])
        i = 0

        while i < len(word) and nodes:

            letter_found = False
            level_size = len(nodes)
            while level_size > 0:
                current = nodes.popleft()
                if word[i] == "." and current.children:
                    letter_found = True
                    nodes.extend(current.children)
                else:
                    for node in current.children:
                        if node.letter == word[i]:
                            letter_found = True
                            nodes.append(node)
                            break

                level_size -= 1

            if letter_found:
                i += 1

        return i == len(word)
