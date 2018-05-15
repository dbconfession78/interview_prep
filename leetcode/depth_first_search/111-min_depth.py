# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        if root is None or root == []:
            return 0
        lvl = 0
        q = [root]
        while q:
            row_len = len(q)
            lvl += 1
            for i in range(row_len):
                top = q[0]
                if top.left is None and top.right is None:
                    return lvl
                for child in (top.left, top.right):
                    if child is not None:
                        q.append(child)
                q = q[1:]








root = TreeNode(None)
print(Solution().minDepth(root))

root = TreeNode(1)
root.left = TreeNode(2)
print(Solution().minDepth(root))

root = TreeNode(0)
print(Solution().minDepth(root))

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
print(Solution().minDepth(root))






#Instructions
"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node. 

For example, the tree below should return 2 since it's first leaf is at the second level

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
"""