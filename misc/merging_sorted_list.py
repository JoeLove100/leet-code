"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing
together the nodes of the first two lists.
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def get_merged_list(node_1: ListNode,
                    node_2: ListNode):

    if node_1 is None:
        return node_2
    if node_2 is None:
        return node_1

    if node_1.val < node_2.val:
        current = node_1
        other = node_2
    else:
        current = node_2
        other = node_1

    initial = current

    while True:

        if current.next is None:
            current.next = other
            break
        elif current.next.val < other.val:
            current = current.next
        else:
            tmp = current.next
            current.next = other
            current = other
            other = tmp

    return initial


def get_merged_list_recursive(node_1: ListNode,
                              node_2: ListNode) -> ListNode:

    if node_1 is None:
        return node_2
    if node_2 is None:
        return node_1

    if node_1.val < node_2.val:
        head = node_1
        node_1 = node_1.next
    else:
        head = node_2
        node_2 = node_2.next

    head.next = get_merged_list_recursive(node_1, node_2)
    return head


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return get_merged_list(l1, l2)


def list_to_linked_list(arr: List[int]) -> ListNode:

    initial = ListNode(arr[0])
    current = initial

    for n in arr[1:]:
        current.next = ListNode(n)
        current = current.next

    return initial


def print_list(node: ListNode):

    while True:
        print(node.val, end="")
        if node.next is None:
            return
        else:
            print("->", end="")
            node = node.next


if __name__ == "__main__":

    import random
    from timeit import default_timer as timer
    random.seed(1234)

    list_1 = list_to_linked_list(sorted([random.randint(1, 100) for _ in range(100)]))
    list_2 = list_to_linked_list(sorted([random.randint(1, 100) for _ in range(100)]))

    t_0 = timer()
    get_merged_list(list_1, list_2)
    t_1 = timer()
    print(f"My method ran in {t_1 - t_0}")

    t_2 = timer()
    get_merged_list_recursive(list_1, list_2)
    t_3 = timer()
    print(f"Recursive method ran in {t_3 - t_2}")


