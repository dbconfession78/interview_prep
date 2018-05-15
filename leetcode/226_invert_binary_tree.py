"""
Invert a binary tree.
     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from data_structures.binary_tree import *


class Solution:
    # def invertTree_PRACTICE(self, root):
    def invertTree(self, root):
        if root is None:
            return None

        right = self.invertTree(root.left)
        left = self.invertTree(root.right)
        root.left = left
        root.right = right
        return root

    def invertTree_Q(self, root):
    # def invertTree(self, root):
        if root is None:
            return root

        stk = [root]
        while stk:
            current = stk.pop(0)
            temp = current.left
            current.left = current.right
            current.right = temp
            if current.left:
                stk.append(current.left)
            if current.right:
                stk.append(current.right)
        return root

    def invertTree_REC(self, root):
    # def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        right = self.invertTree(root.right)
        left = self.invertTree(root.left)

        root.left = right
        root.right = left
        return root


def main():
    bt = build_binary_tree([])
    sys.stdout.write("input: ")
    print_binary_tree(bt)
    sys.stdout.write("output: ")
    print_binary_tree(Solution().invertTree(bt))
    print()
    # [[None]]

    bt = build_binary_tree([4,2,7,1,3,6,9])
    sys.stdout.write("input: ")
    print_binary_tree(bt)
    sys.stdout.write("output: ")
    print_binary_tree(Solution().invertTree(bt))
    print()
    # [[4], [7, 2], [9, 6, 3, 1]]

    bt = build_binary_tree([1,2])
    sys.stdout.write("input: ")
    print_binary_tree(bt)
    sys.stdout.write("output: ")
    print_binary_tree(Solution().invertTree(bt))
    print()
    # [[1], ['null', 2]]

    bt = build_binary_tree([2,3,None,1])
    sys.stdout.write("input: ")
    print_binary_tree(bt)
    sys.stdout.write("output: ")
    print_binary_tree(Solution().invertTree(bt))
    print()
    # [[2], [None, 3], ['null', 'null', 'null', 1]]



#LC Input
# []
# [4,2,7,1,3,6,9]
# [1,2]
# [2,3,null,1]

if __name__ == '__main__':
    main()