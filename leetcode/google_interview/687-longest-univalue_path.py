# Instructions
"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""
import sys
node = 0
trans = False
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        longest = [0]
        self.helper(root, longest)
        return longest[0]

    def helper(self, root, longest):
        if root is None:
            return 0
        left = right = 0

        l_len = self.helper(root.left, longest)
        r_len = self.helper(root.right, longest)

        if root.left and root.left.val == root.val:
            left = l_len + 1
        if root.right and root.right.val == root.val:
            right = r_len + 1

        longest[0] = max(longest[0], right + left)
        return max(right, left)


def print_tree(root):
    if root is None:
        return
    print_tree(root.left)
    print(root.val)
    print_tree(root.right)



def main():
    """
          5
         / \
        4   5
       / \   \
      1   1   5

    """
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right = TreeNode(5)
    root.right.left = None
    root.right.right = TreeNode(5)
    print(Solution().longestUnivaluePath(root))  # 2



    """
          1
         / \
        4   5
       / \   \
      4   4   5

    """
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.left = None
    root.right.right = TreeNode(5)
    print(Solution().longestUnivaluePath(root))  # 2



    """
           5__
         /    \
        4      5
       / \    /
      1   1  5

    """
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right = TreeNode(5)
    root.right.left = TreeNode(5)
    root.right.right = None
    print(Solution().longestUnivaluePath(root))  # 2


    """
            5____
         /       \
        4         5
       / \       /
      1   1     5
               / \
              5   1
             / \   \
            1   5   2

    """
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right = TreeNode(5)
    root.right.left = TreeNode(5)
    root.right.left.left = TreeNode(5)
    root.right.left.left.left = TreeNode(1)
    root.right.left.left.right = TreeNode(5)
    root.right.left.right = TreeNode(1)
    root.right.left.right.right = TreeNode(2)
    print(Solution().longestUnivaluePath(root))  # 4

    root = TreeNode(1)
    print(Solution().longestUnivaluePath(root))  # 0

    root = None
    print(Solution().longestUnivaluePath(root))  # 0

    root = TreeNode(1)
    root.left = TreeNode(1)
    print(Solution().longestUnivaluePath(root))  # 1

    root = TreeNode(1)
    root.left = TreeNode(2)
    print(Solution().longestUnivaluePath(root))  # 0

    """
        1
      /   \
     1     1
    /
   1

    """
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right= TreeNode(1)
    print(Solution().longestUnivaluePath(root))  # 3



    """
        1
      /   \
     1     1

    """
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right= TreeNode(1)
    print(Solution().longestUnivaluePath(root))  # 2


#LC input
# [5,4,5,1,1,null,5]
# [1,4,5,4,4,null,5]
# [5,4,5,1,1,5]
# [5,4,5,1,1,5,null,null, null,null,null,5,1,1,5,null,2]
# [1]
# []
# [1,1]
# [1,2]
# [1,1,1,1]
# [1,1,1]

if __name__ == '__main__':
    main()