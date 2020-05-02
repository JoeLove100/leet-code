"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_half_way_point(node: ListNode) -> ListNode:

    fast = half = node
    counter = 0

    while True:

        if fast.next is None:
            return half

        fast = fast.next
        if counter % 2 == 0:
            half = half.next

        counter += 1


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        return get_half_way_point(head)


def create_linked_list(arr):

    head = ListNode(arr[0])
    current = head
    for n in arr[1:]:
        current.next = ListNode(n)
        current = current.next
    return head


if __name__ == "__main__":

    linked_list = create_linked_list([1, 2, 3, 4])
    result = get_half_way_point(linked_list)
    print(result.val)
