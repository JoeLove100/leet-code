"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

-> The linked list will have at least two elements.
-> All of the nodes' values will be unique.
-> The given node will not be the tail and it will always be a valid node of the linked list.
-> Do not return anything from your function.
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_node(node) -> None:

    while True:

        node.val = node.next.val
        if node.next.next:
            node = node.next
        else:
            node.next = None
            break


class Solution:
    def deleteNode(self, node):
        remove_node(node)


def array_to_linked_list(arr: List[int]) -> ListNode:

    head = ListNode(arr[0])
    current_node = head
    for i in range(1, len(arr)):
        next_node = ListNode(arr[i])
        current_node.next = next_node
        current_node = next_node

    return head


def get_nth_node(node: ListNode,
                 n: int) -> ListNode:

    for _ in range(n):
        node = node.next

    return node


def linked_list_to_array(node) -> List[int]:

    arr = []
    while node:
        arr.append(node.val)
        node = node.next

    return arr



