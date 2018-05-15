"""
Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l1

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[input] linkedlist.integer l2

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[output] linkedlist.integer

A list that contains elements from both l1 and l2, sorted in non-decreasing order.
"""


# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
from data_structures.linked_list import *
def mergeTwoLinkedLists(l1, l2):
    if l1 and not l2:
        return l1
    if not l1 and l2:
        return l2
    w1 = l1
    w2 = l2
    root = ListNode(None)
    w3 = root
    while w1 and w2:
        while w1 and w2 and w2.val < w1.val:
            w3.next = w2
            w3 = w3.next
            prev = w2
            w2 = w2.next
            prev.next = w1

        while w1 and w2 and w1.val <= w2.val:
            w3.next = w1
            w3 = w3.next
            prev = w1
            w1 = w1.next
            prev.next = w2
    return root.next

def main():
    # [1, 2, 3, 4, 5, 6]
    print_linked_list(mergeTwoLinkedLists(
        list_to_linked_list([1,2,3]),
        list_to_linked_list([4,5,6])))

    # [0, 1, 1, 2, 3, 4, 5]
    print_linked_list(mergeTwoLinkedLists(
        list_to_linked_list([1,1,2,4]),
        list_to_linked_list([0,3,5])))

    # [2, 3, 5, 10, 15, 20, 40]
    print_linked_list(mergeTwoLinkedLists(
        list_to_linked_list([5, 10, 15, 40]),
        list_to_linked_list([2,3,20])))

    # [1, 1, 2, 4]
    print_linked_list(mergeTwoLinkedLists(
        list_to_linked_list([1, 1]),
        list_to_linked_list([2,4])))

    # [1, 1, 2, 2, 4, 7, 7, 8]
    print_linked_list(mergeTwoLinkedLists(
        list_to_linked_list([]),
        list_to_linked_list([1, 1, 2, 2, 4, 7, 7, 8])))

    # []
    print_linked_list(mergeTwoLinkedLists(
        list_to_linked_list([]),
        list_to_linked_list([])))

    # [1, 1, 4]
    print_linked_list(mergeTwoLinkedLists(
        list_to_linked_list([1,1,4]),
        list_to_linked_list([])))

    # [0, 1, 1]
    print_linked_list(mergeTwoLinkedLists(
        list_to_linked_list([1,1]),
        list_to_linked_list([0])))

    # [0, 2]
    print_linked_list(mergeTwoLinkedLists(
        list_to_linked_list([0]),
        list_to_linked_list([2])))

    # [-1000000000, 1, 1000000000]
    print_linked_list(mergeTwoLinkedLists(
        list_to_linked_list([1]),
        list_to_linked_list([-1000000000, 1000000000])))

    # [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    print_linked_list(mergeTwoLinkedLists(
        list_to_linked_list([-1,-1,0,1]),
        list_to_linked_list([-1, 0, 0, 1, 1])))

    # [-815817641, -780990573, -670826849, -426491047, -404817961, 242026249, 437929670, 520408640, 731519938]
    print_linked_list(mergeTwoLinkedLists(
        list_to_linked_list([-780990573, -670826849, -404817961, 242026249, 731519938]),
        list_to_linked_list([-815817641, -426491047, 437929670, 520408640])))




if __name__ == '__main__':
    main()