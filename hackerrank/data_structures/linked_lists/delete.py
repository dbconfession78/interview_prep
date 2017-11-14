#!/usr/bin/python3
from linked_list import *


def main():
    head = None
    head = add_tail(head, 1)
    head = add_tail(head, 2)
    head = add_tail(head, 3)
    head = delete(head, 0)
    print_list(head)

def delete(head, position):
    if head is None or head == None:
        return head
    if position == 0:
        head = head.next
        return head
    walk = walk_to(head, position-1)
    walk.next = walk.next.next
    return head


def walk_to(head, position):
    if position == 0:
        return head
    walk = head
    i = 0
    while walk and i != position :
        walk = walk.next
        i += 1
    return walk



if __name__ == '__main__':
    main()
