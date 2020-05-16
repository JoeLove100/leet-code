"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking
about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
"""
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_by_parity(node: ListNode) -> None:

    if node is None or node.next is None:
        return

    pointer_1 = node
    pointer_2 = node.next
    while pointer_2 and pointer_2.next:

        # pop out the next node
        odd_node = pointer_2.next
        pointer_2.next = pointer_2.next.next

        # insert it after pointer 1
        tmp = pointer_1.next
        pointer_1.next = odd_node
        odd_node.next = tmp

        # move the pointers
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        sort_by_parity(head)
        return head

def list_to_linked_list(arr: List[int]) -> ListNode:

    root = ListNode(arr[0])
    current_node = root
    for n in arr[1:]:
        next_node = ListNode(n)
        current_node.next = next_node
        current_node = next_node

    return root


def linked_list_to_list(root: ListNode) -> List[int]:

    output = []
    while root:
        output.append(root.val)
        root = root.next

    return output
