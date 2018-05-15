"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
from data_structures.binary_tree import *


class Solution(object):
    # def buildTree_PRACTICE(self, inorder, postorder):
    def buildTree(self, inorder, postorder):
        return

    def buildTree_SOL(self, inorder, postorder):
    # def buildTree(self, inorder, postorder):
        if inorder:
            idx = inorder.index(postorder.pop())
            root = TreeNode(inorder[idx])
            root.right = self.buildTree(inorder[idx+1:], postorder)
            root.left = self.buildTree(inorder[:idx], postorder)
            return root


def main():
    """
            3
          /  \
        9   20
           /  \
          15  7

    """
    print(levelOrder(Solution().buildTree([9, 3, 15, 20, 7],
                                          [9,15,7,20,3])))


    """
         __ 1______
        /          \
        6_          8___
       /  \       /     \
      4   9      12      14
         / \    /  \    /
        3   7  11   2  70
    """
    print(levelOrder(Solution().buildTree([4, 6, 3, 9, 7, 1, 11, 12, 2, 8, 70, 14],
                                          [4,3,7,9,6,11,2,12,70,14,8,1])))


    print(levelOrder(Solution().buildTree([1],
                                          [])))


    """
            1
             \
              4 
             / 
            3
           / 
          2 
    """
    print(levelOrder(Solution().buildTree([1,2,3,4],
                                          [2,3,4,1])))

#LC input
# [9,3,15,20,7]
# [9,15,7,20,3]
# [4,6,3,9,7,1,11,12,2,8,70,14]
# [4,3,7,9,6,11,2,12,70,14,8,1]
# [1]
# []
# [1,2,3,4]
# [2,3,4,1]

if __name__ == '__main__':
    main()