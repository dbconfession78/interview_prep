#!/usr/bin/python3
from print_ll import print_list
from node import Node

def main():
    head = Node()
    head = Insert(None, 5)
    head = Insert(head, 7)
    walk = head
    print_list(head)
 

def Insert(head, data):
    node = Node(data)
    if head is None:
        head = node
        return head
    walk = head
    if walk.data == None:
        head = node
        return head

    while walk:
        if walk.next:
            walk = walk.next
        else:
            walk.next = node
            break

    return head
    


if __name__ == '__main__':
    main()
