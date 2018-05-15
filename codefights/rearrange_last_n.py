"""
Note: Try to solve this task in O(list size) time using O(1) additional space, since this is what you'll be asked during an interview.

Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning of the linked list.

Example

For l = [1, 2, 3, 4, 5] and n = 3, the output should be
rearrangeLastN(l, n) = [3, 4, 5, 1, 2];
For l = [1, 2, 3, 4, 5, 6, 7] and n = 1, the output should be
rearrangeLastN(l, n) = [7, 1, 2, 3, 4, 5, 6].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 105,
-1000 ≤ element value ≤ 1000.

[input] integer n

A non-negative integer.

Guaranteed constraints:
0 ≤ n ≤ list size.

[output] linkedlist.integer

Return l with the n last elements moved to the beginning.
"""
# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
from data_structures.linked_list import *
# def rearrangeLastN_PRACTICE(l, n):
def rearrangeLastN(l, n):
    return

def rearrangeLastN_SOL(l, n):
# def rearrangeLastN(l, n):
    if not l or not l.next or n <= 0:
        return l
    w1 = l
    w2 = l
    prev = None
    i = 0
    while w1.next:
        if i < n-1:
            i += 1
        else:
            prev = w2
            w2 = w2.next
        w1 = w1.next
    if i < n-1:
        return l
    if prev:
        prev.next = None
    else:
        return l
    w1.next = l
    l = w2
    return l



def main():
    # [3, 4, 5, 1, 2]
    print_linked_list(rearrangeLastN(list_to_linked_list([1, 2, 3, 4, 5]), 3))

    # [7,1,2,3,4,5,6]
    print_linked_list(rearrangeLastN(list_to_linked_list([1, 2, 3, 4, 5, 6, 7]), 1))

    # [6,7,1,2,3,4,5]
    print_linked_list(rearrangeLastN(list_to_linked_list([1, 2, 3, 4, 5, 6, 7]), 2))

    # [7,8,9,10,1,2,3,4,5,6]
    print_linked_list(rearrangeLastN(list_to_linked_list([1, 2, 3, 4, 5,6,7,8,9,10]), 4))

    # [1000, -1000]
    print_linked_list(rearrangeLastN(list_to_linked_list([1000, -1000]), 0))

    # [123, 456, 789, 0]
    print_linked_list(rearrangeLastN(list_to_linked_list([123, 456, 789, 0]), 4))

if __name__ == '__main__':
    main()

