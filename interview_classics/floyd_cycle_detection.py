"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in
the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def is_cycle(node: ListNode) -> bool:
    """
    find if there is a cycle using
    Floyd's cycle detection algorithm
    """

    if node is None:
        return False

    slow = node
    fast = node

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True

    return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        return is_cycle(head)


def list_to_linked_list(arr: List[int],
                        pos) -> ListNode:

    initial = ListNode(arr[0])
    current = initial
    all_nodes = []

    for n in arr[1:]:
        all_nodes.append(current)
        current.next = ListNode(n)
        current = current.next

    if pos is not None:
        current.next = all_nodes[pos]

    return initial


if __name__ == "__main__":

    l_1 = list_to_linked_list([1, 2, 3, 4, 5], 3)
    print(is_cycle(l_1))

