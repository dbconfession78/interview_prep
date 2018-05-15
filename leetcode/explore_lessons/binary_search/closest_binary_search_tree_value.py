"""
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""

from data_structures.binary_search_tree import *
from data_structures.binary_tree import print_binary_tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root.left or root.right:
            return self.helper(root, target, None)
        else:
            return root.val

    def helper(self, root, target, retval):
        if root and root.val or (root and root.val == 0):
            l = root.left
            r = root.right
            if root.left is None and root.right is None:
                diff_a  = abs(target - root.val)
                diff_b  = abs(target - retval)
                if diff_a < diff_b:
                    return root.val
                return retval


            if retval is None:
                retval = root.val
            else:
                diff_a = abs(target - root.val)
                diff_b = abs(target - retval)
                if diff_a < diff_b:
                    retval = root.val

            left = self.helper(root.left, target, retval)
            right = self.helper(root.right, target, retval)

            l_diff = abs(target - left)
            r_diff = abs(target - right)
            if l_diff < r_diff:
                closer = left
            else:
                closer = right

            diff_a = abs(target - closer)
            diff_b = abs(target - retval)
            if diff_a < diff_b:
                return closer
        return retval





def main():
    bst = build_bst([1])
    # print_binary_tree(bst.root)
    print(Solution().closestValue(bst.root, 4.428571))    # 1

    bst = build_bst([50,25,75,12.5,35,70,100,6.25,13,17.5,45,60,74,80,125])
    print(Solution().closestValue(bst.root, 4.428571))      # 6.25

    bst = build_bst([50,25,75,12.5,35,70,100,6.25,13,17.5,45,60,74,80,125])
    print(Solution().closestValue(bst.root, 14.24))      # 13

    bst = build_bst([2,1])
    print(Solution().closestValue(bst.root, 2147483647.0))      # 2


    root = BST_node(3)
    root.left = BST_node(1)
    root.right = BST_node(4)
    root.left.right = BST_node(2)
    print(Solution().closestValue(root, 0.428571))          # 1
    
    
    root = BST_node(2)
    root.left = BST_node(0)
    root.right = BST_node(33)
    root.left.right = BST_node(1)
    root.right.left = BST_node(25)
    root.right.right = BST_node(40)
    # print_binary_tree(root)
    print(Solution().closestValue(root, 0.428571))  # 0



# LC Input
# [1]
# 4.428571
# [50,25,75,12.5,35,70,100,6.25,13,17.5,45,60,74,80,125]
# 4.428571
# [50,25,75,12.5,35,70,100,6.25,13,17.5,45,60,74,80,125]
# 14.24
# [2,1]
# 2147483647.0
# [3,1,4,null,2]
# 0.428571
# [2,0,33,null,1,25,40,null,null,11,31,34,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,35,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,null,null,38,null,41,null,null,null,47,49,null,null,5,null,13,15,21,23,null,28,37,null,null,null,null,null,null,null,null,8,null,null,null,17,19,null,null,null,null,null,null,null,7,null,16,null,null,20,6]
# 0.428571

if __name__ == '__main__':
    main()