#!/usr/bin/python3
from linked_list import *


def main():
    print('head1\n-----')
    head1 = None
    head1 = add_tail(head1, 1)
    head1 = add_tail(head1, 3)
    head1 = add_tail(head1, 5)
    head1 = add_tail(head1, 6)
    print_list(head1)

    print('head2\n-----')
    head2 = None
    head2 = add_tail(head2, 2)
    head2 = add_tail(head2, 4)
    head2 = add_tail(head2, 7)
    print_list(head2)

    merged = merge_lists(head1, head2)
    print_list(merged)

def merge_lists(headA, headB):
    if not headA and not headB:
        return None

    if headA and not headB:
        return headA

    if headB and not headA:
        return headB

    if headA.data < headB.data:
        lesser = headA
        lesser.next = merge_lists(headA.next, headB)
    elif headB.data < headA.data:
        lesser = headB
        lesser.next = merge_lists(headA, headB.next)

    return lesser
        

if __name__ == '__main__':
    main()
