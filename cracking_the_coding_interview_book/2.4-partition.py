# Instructions
"""
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.  If x is contained within the list, the values of x only need to be after the elements less than x (see below).  The partition element x can appear anywhere in the "right partition"; it doesn't need to appear between the left and right partitions.

e.g.
Input:   3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1  [partition=5]
Output:  3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""

from data_structures.linked_list import *
class Solution:
    def partition_BOOK(self, root, partition):
    # def partition(self, root, partition):
        w = root
        before_start = None
        before_end = None
        after_start = None
        after_end = None

        while w is not None:
            next = w.next
            w.next = None
            if w.val < partition:
                if before_start is None:
                    before_start = w
                    before_end = before_start
                else:
                    before_end.next = w
                    before_end = w
            else:
                if after_start is None:
                    after_start = w
                    after_end = after_start
                else:
                    after_end.next = w
                    after_end = w
            w = next

        if before_start is None:
            return after_start

        before_end.next = after_start
        return before_start

    # def partition_MINE(self, root, partition):
    def partition(self, root, partition):
        left = None
        l_w = None
        right = None
        r_w = None

        w = root

        while w:
            if w.val < partition:
                if left is None:
                    left = ListNode(w.val)
                    l_w = left
                else:
                    l_w.next = ListNode(w.val)
                    l_w = l_w.next
            if w.val >= partition:
                if right is None:
                    right = ListNode(w.val)
                    r_w = right
                else:
                    r_w.next = ListNode(w.val)
                    r_w = r_w.next

            w = w.next

        l_w.next = right

        root.val = left.val
        root.next = left.next


def main():
    root = list_to_linked_list([3, 5, 8, 5, 10, 2, 1])
    Solution().partition(root, 5)
    print_linked_list(root)

    root = list_to_linked_list([3, 5, 8, 5, 10, 2, 1])
    Solution().partition(root, 5)
    print_linked_list(root)


if __name__ == '__main__':
    main()