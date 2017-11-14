#!/usr/bin/python3
from linked_list import *
from node import Node


def main():
    head = None
    head = insert_nth(head, 3, 0)
    head = insert_nth(head, 4, 0)
    head = insert_nth(head, 7, 1)
    

    print_list(head)
    

def insert_nth(head, data, position):
    i = 0
    node = Node(data)
    walk = head
    if head == None:
        head = node
        return head
    if position == 0:
        head = add_head(head, data)
        return head
    while walk:
        if i+1 == position:
            node.next = walk.next
            walk.next = node
            return head
        walk = walk.next
        i += 1
    return head
        





if __name__ == '__main__':
    main()
