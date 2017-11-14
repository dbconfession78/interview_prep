#!/usr/bin/python3
from node import Node
import sys


def add_head(head, data):
    node = Node(data)
    if head == None:
        head = node
        return head

    node.next = head
    head = node
    return head


def add_tail(head, data):
    node = Node(data)
    if head is None:
        head = node
        return head

    
    walk = walk_to_tail(head)
    node.prev = walk
    walk.next = node
    return head

def insert_node(head, data, position):
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


def delete_node(head, position):
    if head is None or head == None:
        return head
    if position == 0:
        head = head.next
        return head
    walk = walk_to(head, position-1)
    walk.next = walk.next.next
    return head


def walk_to_index(head, position):
    if position == 0:
        return head
    walk = head
    i = 0
    while walk and i != position:
        walk = walk.next
        i += 1
    return walk

def walk_to_tail(head):
    while head.next:
        head = head.next
    return head

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

def reverse_print(head):
    walk = walk_to_tail(head)
    while walk:
        print(walk.data)
        walk = walk.prev

def count(head):
    walk = head
    count = 0
    while walk:
        count += 1
        walk = walk.next
    return count

def print_list(head):
    walk = head
    is_head = True
    while walk:
        sys.stdout.write('{}'.format(walk.data))
        if is_head:
            sys.stdout.write(' <---- head')
        print()
        is_head = False
        walk = walk.next
