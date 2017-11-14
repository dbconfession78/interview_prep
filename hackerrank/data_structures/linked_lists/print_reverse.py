#!/usr/bin/python3
from linked_list import *


def main():
    head = None
    head = add_tail(head, 1)
    head = add_tail(head, 2)
    head = add_tail(head, 3)
    walk = walk_to_tail(head)
    reverse_print_sll(head)


# assumes doubly linked list
def reverse_print_dll(head):
    walk = walk_to_tail(head)
    while walk:
        print(walk.data)
        walk = walk.prev

# asdsumes singly linked list
def reverse_print_sll(head):
    to_print = []
    walk = head
    i = count(head) - 1
    while i >= 0:
        walk = walk_to_index(head, i)
        print(walk.data)
        i -= 1


if __name__ == '__main__':
    main()
