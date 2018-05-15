"""
Sort a linked list in O(n log n) time using constant space complexity.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from data_structures.linked_list import *
class Solution:
    # def sortList_PRACTICE(self, head):
    def sortList(self, head):
        return

    def sortList_SOL(self, head):
    # def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge_sort(node):
            if not node or not node.next:
                return node

            mid = get_mid_node(node)
            right_start = mid.next
            mid.next = None
            left = merge_sort(node)
            right = merge_sort(right_start)
            return sortedMerge(left, right)

        def sortedMerge(a, b):
            """ Base cases """
            if a is None:
                return b
            if b is None:
                return a

            if a.val <= b.val:
                result = a
                result.next = sortedMerge(a.next, b)
            else:
                result = b
                result.next = sortedMerge(a, b.next)

            return result

        def get_mid_node(head):
            fst = head.next
            slw = head

            while fst.next:
                fst = fst.next
                if fst.next:
                    fst = fst.next
                    slw = slw.next
            return slw

        return merge_sort(head)


def main():
    print_linked_list(Solution().sortList(list_to_linked_list([2,67,8,3,67,8,4,3,19,8])))


if __name__ == '__main__':
    main()

