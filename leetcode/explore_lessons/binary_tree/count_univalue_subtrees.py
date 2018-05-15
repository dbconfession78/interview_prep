"""
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,
              5
             / \
            1   5
           / \   \
          5   5   5
return 4.
"""

from data_structures.binary_tree import *
class Solution:
    # def countUnivalSubtrees_PRACTICE(self, root):
    def countUnivalSubtrees(self, root):
        return

    # def countUnivalSubtrees_SOL(self, root):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0

        def is_uni(root):
            if root is None:
                return True
            left = is_uni(root.left)
            right = is_uni(root.right)
            if left and right:
                if root.left is None or root.left.val == root.val:
                    if root.right is None or root.right.val == root.val:
                        self.count += 1
                        return True
            return False

        is_uni(root)
        return self.count


def main():
    # 4
    print(Solution().countUnivalSubtrees(build_binary_tree([5, 1, 5, 5, 5, None, 5])))





# LC input
# [5,1,5,5,5,null,5]

if __name__ == '__main__':
    main()