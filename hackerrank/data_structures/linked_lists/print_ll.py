#!/usr/bin/python3

def print_list(head):
    walk = head
    while walk:
        print(walk.data)
        walk = walk.next
