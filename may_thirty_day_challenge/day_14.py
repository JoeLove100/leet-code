"""
Implement a trie with insert, search, and startsWith methods.
"""


class Node:

    def __init__(self,
                 letter: str):

        self.letter = letter
        self.children = []


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self._root = Node("")
        self._special_char = "$"

    def insert(self,
               word: str) -> None:
        """
        Inserts a word into the trie.
        """

        word += self._special_char
        current_node = self._root

        for letter in word:

            matched = False
            for child in current_node.children:
                if letter == child.letter:
                    matched = True
                    current_node = child
                    break

            if not matched:
                new_node = Node(letter)
                current_node.children.append(new_node)
                current_node = new_node

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        word += self._special_char
        return self.startsWith(word)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        current = self._root

        for letter in prefix:
            matched = False
            for child in current.children:
                if letter == child.letter:
                    matched = True
                    current = child
                    break

            if not matched:
                return False

        return True
