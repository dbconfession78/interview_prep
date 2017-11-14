#!/usr/bin/python3
from linked_list import *


def main():
    head = None
    head = add_tail(head, 1)
    head = add_tail(head, 2)
    head = add_tail(head, 3)
    head = add_tail(head, 4)
    head = add_tail(head, 5)
    head = add_tail(head, 6)
    print_list(head)
    head = reverse(head)
    print_list(head)

#    print_list(head)

def reverse(head):
    if head is None:
        return head
    i = count(head)-1
    new_head = walk_to_tail(head)
    walk = new_head
    while i >= 0:
        next = walk_to_index(head, i)
        walk.next = next
        walk = walk.next
        i -= 1
    walk.next = head
    walk.next.next = None
    return new_head


if __name__ == '__main__':
    main()
