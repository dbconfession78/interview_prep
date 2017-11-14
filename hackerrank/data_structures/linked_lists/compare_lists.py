#!/usr/bin/python3
from linked_list import *


def main():
    print('head1\n-----')
    head1 = None
    head1 = add_tail(head1, 1)
    head1 = add_tail(head1, 2)
    head1 = add_tail(head1, 3)
    print_list(head1)

    print('head2\n-----')
    head2 = None
    head2 = add_tail(head2, 1)
    head2 = add_tail(head2, 2)
    head2 = add_tail(head2, 3)
    print_list(head2)

    print(compare_lists(head1, head2))

def compare_lists(headA, headB):
    if headA is None or headB is None:
        return False

    if count(headA) != count(headB):
        return False
    
    while headA and headB:
        if headA.data != headB.data:
            return False
        headA = headA.next
        headB = headB.next
        

    return True

if __name__ == '__main__':
    main()
