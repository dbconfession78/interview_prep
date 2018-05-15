"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Example:
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from data_structures.linked_list import *
from data_structures.binary_search_tree import *
from data_structures.binary_tree import *
class Solution:
    # def sortedListToBST_PRACTICE(self, head):
    def sortedListToBST(self, head):
        return

    def sortedListToBST_REC(self, head):
    # def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)

        slow = head
        fast = head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tmp = slow.next
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root






def main():
    # print_binary_tree(Solution().sortedListToBST(list_to_linked_list([-10,-3,0,5,9])))
    # [0, -3, 9, -10, '_', 5, '_']

    bst = Solution().sortedListToBST(list_to_linked_list([-30, -25, -24, -20, -15, -10, -3, 0, 5, 9, 15, 20, 100, 101, 102]))
    print_binary_tree(bst)
    # [0, -20, 20, -25, -10, 9, 101, -30, -24, -15, -3, 5, 15, 100, 102]

    # print_binary_tree(Solution().list_to_linked_list([]))
    # # ['_']


# LC Input
# [-10,-3,0,5,9]
# [-30, -25, -24, -20, -15, -10, -3, 0, 5, 9, 15, 20, 100, 101, 102]
# []


if __name__ == '__main__':
    main()
