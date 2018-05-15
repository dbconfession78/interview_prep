"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.


Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from data_structures.binary_tree import *


class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        _len = len(nums)

        if _len == 1:
            return TreeNode(nums[0])

        mid_i = _len // 2
        mid_v = nums[mid_i]
        node = TreeNode(mid_v)
        left_lst = nums[0:mid_i]
        right_lst = nums[mid_i+1:]
        node.left = self.sortedArrayToBST(left_lst)
        node.right = self.sortedArrayToBST(right_lst)
        return node


def main():
    print_binary_tree(Solution().sortedArrayToBST([-10,-3,0,5,9]))
    # [0, -3, 9, -10, '_', 5, '_']

    print_binary_tree(Solution().sortedArrayToBST([-30, -25, -24, -20, -15, -10, -3, 0, 5, 9, 15, 20, 100, 101, 102]))
    # [0, -20, 20, -25, -10, 9, 101, -30, -24, -15, -3, 5, 15, 100, 102]

    print_binary_tree(Solution().sortedArrayToBST([]))
    # ['_']


# LC Input
# [-10,-3,0,5,9]
# [-30, -25, -24, -20, -15, -10, -3, 0, 5, 9, 15, 20, 100, 101, 102]
# []


if __name__ == '__main__':
    main()
