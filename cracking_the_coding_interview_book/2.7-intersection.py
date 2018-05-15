# Instructions
"""
Given two sll's, determine if the two lists intersect.  Return the intersecting node.  Note that the intersection is defined based on the reference, not value.  That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
"""
from data_structures.linked_list import *


class Solution:
    def intersection(self, r1, r2):
        w1 = r1
        w2 = r2

        while w1 and w2:
            if w1 == w2:
                return w1
            w1 = w1.next
            w2 = w2.next
        return None


def main():
    r1 = ListNode('C')
    r1.next = ListNode('A')
    r1.next.next = ListNode('T')

    r1.next.next.next = ListNode('S')

    r2 = ListNode('B')
    r2.next = ListNode('A')
    r2.next.next = ListNode('T')
    r2.next.next.next = r1.next.next.next
    print(Solution().intersection(r1, r2).val)




if __name__ == '__main__':
    main()