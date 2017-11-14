#!/usr/bin/python3
from node import Node
from print_ll import print_list


def main():
    head = Insert(None, 5)
    head = Insert(head, 7)
    print_list(head)


def Insert(head, data):
    node = Node(data)
    if head == None:
        head = node
        return head

    node.next = head
    head = node
    return head


if __name__ == '__main__':
    main()
