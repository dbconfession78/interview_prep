# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def isSameTree_PRACTICE(self, p, q):
    def isSameTree(self, p, q):
        return



    def isSameTree_PASSED(self, p, q):
    # def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False

        if p.val != q.val:
            return False

        l = self.isSameTree(p.left, q.left)
        if l is False:
            return False
        r = self. isSameTree(p.right, q.right)
        if r == False:
            return False

        return True



def main():
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    print(Solution().isSameTree(p, q))  # True

    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    p.right.right = TreeNode(4)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    q.right.right = TreeNode(1)
    print(Solution().isSameTree(p, q))  # False

    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    p.right.right = TreeNode(4)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    q.right.right = TreeNode(4)
    print(Solution().isSameTree(p, q))  # True

    p = TreeNode(1)
    p.left = TreeNode(2)

    q = TreeNode(1)
    q.right = TreeNode(1)
    print(Solution().isSameTree(p, q))  # False

# LC input
# [1,2,3]
# [1,2,3]
# [1,2,3,null,null,null,4]
# [1,2,3,null,null,null,1]
# [1,2,3,null,null,null,4]
# [1,2,3,null,null,null,4]
# [1,2]
# [1,null,2]

if __name__ == '__main__':
    main()

# Instructions
"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.


Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""