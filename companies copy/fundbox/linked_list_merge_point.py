# Linked List Merge Point
"""
Find point where two linked lists merge
"""
import sys
# from data_structures.linked_list import *
from data_structures.linked_list import list_to_linked_list, append_node_to_linked_list, print_linked_list
from collections import defaultdict

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.length = 0
        self.root = None
        self.tail = None

    def add_node_by_data_struct(self, node):
        self.tail.next = node
        self.tail = self.tail.next
        self.length += 1

    def add_node_by_val(self, val):
        new = ListNode(val)
        if self.root is None:
            self.root = new
            self.tail = self.root
        else:
            self.tail.next = new
            self.tail = self.tail.next
        self.length += 1

    def get_length(self):
        return self.length

    def print(self):
        if self.root is None:
            print('[]')
            return
        sys.stdout.write('[')
        w = self.root
        while w:
            sys.stdout.write(str(w.val))
            if w.next:
                sys.stdout.write(', ')
            else:
                sys.stdout.write(']\n')
            w = w.next

    def update(self):
        while self.tail.next:
            self.length += 1
            self.tail = self.tail.next


class Solution():
    # def get_merge_point_PRACTICE(self, l1, l2):
    def get_merge_point(self, l1, l2):
        len1 = l1.get_length()
        len2 = l2.get_length()
        diff = abs(len2 - len1)
        w = l1.root if len1 < len2 else l2.root
        i = min(len1, len2)
        while i != diff:
            w = w.next
            i -= 1
        return w


def main():
    hub = ListNode(6)
    ll1 = LinkedList()
    ll2 = LinkedList()

    lst1 = [1, 2, 3, 4, 5, 14, 8, 11]
    for n in lst1:
        ll1.add_node_by_val(n)
    ll1.add_node_by_data_struct(hub)

    lst2 = [10, 9, 8, 7]
    for n in lst2:
        ll2.add_node_by_val(n)
    ll2.add_node_by_data_struct(hub)

    mut0 = ListNode(3)
    mut1 = ListNode(4)
    mut2 = ListNode(5)

    ll2.add_node_by_data_struct(mut0)
    ll2.add_node_by_data_struct(mut1)
    ll2.add_node_by_data_struct(mut2)
    ll1.update()

    ll1.print()
    ll2.print()
    print(Solution().get_merge_point(ll1, ll2).val)   # 6


if __name__ == '__main__':
    main()