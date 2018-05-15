"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
from data_structures.binary_tree import *


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[idx])

            root.left = self.buildTree(preorder, inorder[:idx])
            root.right = self.buildTree(preorder, inorder[idx+1:])
            return root


def main():
    """
            3
          /  \
        9   20
           /  \
          15  7

    """
    # print(levelOrder(Solution().buildTree([3,9,20,15,7],
    #                                       [9,3,15,20,7])))

    print(levelOrder(Solution().buildTree([1, 2, 4, 3, 5, 6],
                                          [4, 2, 1, 5, 3, 6])))

if __name__ == '__main__':
    main()