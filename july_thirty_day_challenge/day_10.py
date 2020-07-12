"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer,
which may or may not point to a separate doubly linked list. These child lists may have one or more children of
their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of
the first level of the list.
"""

from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def get_flattened_list(root: Optional[Node]) -> Optional[Node]:

    if not root:
        return root

    stack = []
    current = root
    while True:
        if current.next and not current.child:
            current = current.next
        elif current.child:
            if current.next:
                stack.append(current.next)
            current.next = current.child
            current.next.prev = current  # this seems to be required on leet code for some reason
            current.child = None
            current = current.next
        else:
            if not stack:
                break
            else:
                next_node = stack.pop()
                current.next, next_node.prev = next_node, current
                current = next_node

    return root


class Solution:
    def flatten(self, head: Node) -> Node:
        return get_flattened_list(head)
