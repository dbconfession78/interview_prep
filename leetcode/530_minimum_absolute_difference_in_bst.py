"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.
"""


# Definition for a binary tree node.
from data_structures.binary_search_tree import *
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # def getMinimumDifference_PRACTICE(self, root):
    def getMinimumDifference(self, root):
        return


    def getMinimumDifference_PASSED(self, root):
    # def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, cache, retval):
            if root is None:
                return retval

            if root.left:
                retval = dfs(root.left, cache, retval)
            cache.append(root.val)
            if len(cache) > 1:
                diff = abs(cache[-1] - cache[-2])
                retval = min(retval, diff)
            if root.right:
                retval = dfs(root.right, cache, retval)
            return retval

        return dfs(root, [], float('inf'))

def main():
    root = build_bst([1,3,2]).root
    print(Solution().getMinimumDifference(root))    # 1

    root = build_bst(([100,50,40,30,60,45,55,70,200,250,260,198,140,199,240])).root
    print(Solution().getMinimumDifference(root))    # 1

    root = build_bst([236,104,227,701,911]).root
    print(Solution().getMinimumDifference(root))    # 9


# LC input
# [1,null,3,2]
# [100,50,40,30,60,45,55,70,200,250,260,198,140,199,240]
# [236,104,701,null,227,null,911]

if __name__ == '__main__':
    main()