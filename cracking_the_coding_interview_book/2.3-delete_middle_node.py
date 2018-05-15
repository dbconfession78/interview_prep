# Instructions
"""
Impement an algorithm to delete a node at the middle (i.e. any node but the first and last node, not necessarily the exact middle) of a sll, given access to that node.

e.g.
input: node C from sll A->B->C->D->E->F
Result: no return, but sll now is A->B->D->E->->F
"""
from data_structures.linked_list import *


class Solution:
    def delete_middle_node(self, m):
        if not m or not m.next:
            return None

        m.val = m.next.val
        m.next = m.next.next


def main():
    root = list_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    mid_node = get_mid_node(root)
    print(f'mid: {mid_node.val}')
    Solution().delete_middle_node(mid_node)
    print_linked_list(root)

    root = list_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    mid_node = get_mid_node(root)
    print(f'mid: {mid_node.val}')
    Solution().delete_middle_node(mid_node)
    print_linked_list(root)


def get_mid_node(root):
    w = root
    _len = 0
    while w:
        w = w.next
        _len += 1
    w = root
    i = 0
    while w and i < _len // 2:
        w = w.next
        i += 1
    return w


if __name__ == '__main__':
    main()