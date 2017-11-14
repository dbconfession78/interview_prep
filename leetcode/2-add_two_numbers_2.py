#!/usr/bin/python3
from linked_list import *

def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    l3 = LinkedList()
    w1 = l1.root
    w2 = l2.root
    carry = 0
    d1 = 0
    d2 = 0

    while(w1 is not None or w2 is not None or carry != 0):
        input('w1: {}\nw2: {}\ncarry: {}'.format(w1, w2, carry))

        d1 = 0; d2 = 0;
        if w1 is not None:
            d1 = w1.data
        if w2 is not None:
            d2 = w2.data

        sum = int(d1 + d2 + carry)
        carry = 0
        if sum > 9:
            carry = int(sum / 10)
            sum = int(sum % 10)

        l3.add(sum)
        if w1 is not None:
            w1 = w1.next
        if w2 is not None:
            w2 = w2.next

    return l3


def main():
    l1 = LinkedList()
    l1.add(5)
    l1.print_ll()


    l2 = LinkedList()
    l2.add(5)
    l2.print_ll()

    l3 = add_two_numbers(l1, l2)
    l3.print_ll()
if __name__ == '__main__':
    main()
