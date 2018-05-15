import sys
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2:
            return l2
        if l2 is None and l1:
            return l1
        if l1 is None and l2 is None:
            return None
        w1 = l1
        w2 = l2
        w3 = ListNode(None)
        first = True
        while w1 and w2:
            v1 = w1.val; v2 = w2.val
            if v1 < v2:
                lo = v1
                w1 = w1.next
            else:
                lo = v2
                w2 = w2.next
            if first:
                first = False
                l3 = ListNode(lo)
                w3 = l3
            else:
                w3.next = ListNode(lo)
                w3 = w3.next
        while w1:
            w3.next = ListNode(w1.val)
            w3 = w3.next
            w1 = w1.next
        while w2:
            w3.next = ListNode(w2.val)
            w3 = w3.next
            w2 = w2.next

        return l3

def main():
    """Test cases"""
    # case
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    print_ll(Solution().mergeTwoLists(l1, l2))

    # case
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    print_ll(Solution().mergeTwoLists(l1, l2))


    # case
    print_ll(Solution().mergeTwoLists(None, l2))

    # case
    print_ll(Solution().mergeTwoLists(None, None))

    # case
    l1 = ListNode(5)
    l2 = ListNode(1)

    l2.next = ListNode(2)
    l2.next.next = ListNode(4)
    print_ll(Solution().mergeTwoLists(l1, l2))


def print_ll(root):
    if root is None:
        print('[]')
        return
    w = root
    sys.stdout.write('[')
    while w:
        sys.stdout.write(str(w.val))
        if w.next:
            sys.stdout.write(', ')
        else:
            sys.stdout.write(']')
        w = w.next
    print()

if __name__ == '__main__':
    main()

# expected
# [1, 1, 2, 3, 4, 4]
# [1, 1, 2, 3, 4, 4, 5]
# [1, 3, 4]
# []
# [1, 2, 4, 5]

# LC input
# [1,2,4]
# [1,3,4]
# [1,2,4,5]
# [1,3,4]
# []
# [1,3,4]
# []
# []
# [5,1]
# [2,4]

# Instructions:
"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""