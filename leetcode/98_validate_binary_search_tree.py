"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from data_structures.binary_search_tree import *
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        cache, counter, has_dupe = self.helper(root, [], set(), False)
        if has_dupe:
            return False
        return True if cache == sorted(cache) else False

    def helper(self, root, cache, counter, has_dupe):
        if root is None or has_dupe:
            return cache, counter, has_dupe

        cache, counter, has_dupe = self.helper(root.left, cache, counter, has_dupe)
        if has_dupe:
            return cache, counter, has_dupe

        cache.append(root.val)
        if root.val in counter:
            has_dupe = True
        else:
            counter.add(root.val)

        cache, counter, has_dupe = self.helper(root.right, cache, counter, has_dupe)
        if has_dupe:
            return cache, counter, has_dupe

        return cache, counter, has_dupe

def main():

    # True
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(Solution().isValidBST(root))

    # False
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    print(Solution().isValidBST(root))

    # False
    root = TreeNode(100)
    root.left = TreeNode(50)
    root.right = TreeNode(200)
    root.left.left = TreeNode(45)
    root.left.right = TreeNode(101)
    print(Solution().isValidBST(root))

    # False
    root = TreeNode(1)
    root.left = TreeNode(1)
    print(Solution().isValidBST(root))


# LC Input
# [2,1,3]
# [2,1,3,3,4]
# [100, 50, 200, 45, 101]
# [1,1]

if __name__ == '__main__':
    main()
