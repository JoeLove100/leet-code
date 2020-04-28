"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in
the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
"""
from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_cycle_start(root: ListNode) -> Optional[ListNode]:
    """
    find if there is a cycle using
    Floyd's cycle detection algorithm
    """

    if root is None:
        return None

    slow = root
    fast = root

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            break

    if not fast.next or not fast.next.next:
        return None
    else:
        slow = root
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        return get_cycle_start(head)


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

    l_1 = list_to_linked_list([3, 2, 0, -4], 1)
    n = get_cycle_start(l_1)
    print(n)

