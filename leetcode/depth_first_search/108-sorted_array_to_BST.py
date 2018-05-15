# from data_structures.binary_tree import *
# Instructions:
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
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        if nums == []:
            return None
        mid_idx = len(nums) // 2
        root = TreeNode(nums[mid_idx])
        root.left = self.sortedArrayToBST(nums[:mid_idx])
        root.right = self.sortedArrayToBST(nums[mid_idx+1:])
        return root



    def sortedArrayToBST2(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        arr_len = len(nums)
        if arr_len == 0:
            return None

        root = TreeNode(nums[0])
        for i in range(arr_len[1:]):
            if root.left is None:
                root.left = TreeNode(0)

        mid_idx = len(nums) // 2
        root = TreeNode(nums[mid_idx])
        if arr_len == 1:
            return root
        left_stk = nums[:mid_idx]
        right_stk = nums[mid_idx+1:]

        walk = root
        while left_stk:
            walk.left = TreeNode(left_stk.pop())
            walk = walk.left


        walk = root
        walk.right = TreeNode(right_stk.pop())
        walk = walk.right
        while right_stk:
            new = TreeNode(right_stk.pop())
            if walk.left is None:
                walk.left = new
            else:
                walk.right = new
                walk = walk.left



        print(is_balanced(root))


def in_order(root):
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)


def main():
    # case 1
    nums = [-10,-3,0,5,9]
    tree = Solution().sortedArrayToBST(nums)
    in_order(tree)





if __name__ == '__main__':
    main()
