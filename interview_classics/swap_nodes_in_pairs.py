"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swap_all_nodes(node: ListNode):

    if node is None:
        return None

    prev_node = None
    current_node = node
    next_node = node.next

    if next_node is None:
        return node
    else:
        head = next_node

    while True:

        # do the current swap
        tmp = next_node.next
        next_node.next = current_node
        current_node.next = tmp
        if prev_node:
            prev_node.next = next_node

        # move pointers
        prev_node = current_node
        current_node = current_node.next
        if current_node is None:
            return head

        next_node = current_node.next
        if next_node is None:
            return head


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        return swap_all_nodes(head)


def create_linked_list(arr):

    head = ListNode(arr[0])
    current = head
    for n in arr[1:]:
        current.next = ListNode(n)
        current = current.next
    return head


def print_linked_list(head):

    current_node = head
    while True:
        print(current_node.val, end="")

        if current_node.next:
            print("->", end="")
            current_node = current_node.next
        else:
            return


if __name__ == "__main__":

    linked_list = create_linked_list([1, 2, 6])
    h = swap_all_nodes(linked_list)
    print_linked_list(h)

