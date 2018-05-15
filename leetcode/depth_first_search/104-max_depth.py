# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def maxDepth_PRACTICE(self, root):
    def maxDepth(self, root):
        stk = [root]
        height = 0
        while stk:
            stk_len = len(stk)
            height += 1
            for i in range(stk_len):
                top = stk.pop()
                for child in (top.left, top.right):
                    if child:
                        stk.insert(0, child)
        return height




    def maxDepth_PASSED(self, root):
    # def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        l = self.maxDepth(root.left) + 1
        r = self.maxDepth(root.right) + 1

        return max(l, r)


def main():
    # root = None
    # print(Solution().maxDepth(root))    # 0


    """
        0____
      /      \
     1       2_
    / \     /  \
   3   4   6    5
        \   \
         5   7
          \
           5
    """
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.right.right = TreeNode(5)
    root.left.right.right.right = TreeNode(5)
    root.right.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.left.right = TreeNode(7)
    print(Solution().maxDepth(root))        # 5

# LC input
# []
# [0,1,2,3,4,6,5,null,null,null,5,null,7,null,null,null,5]
if __name__ == '__main__':
    main()


# Instructions:
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""