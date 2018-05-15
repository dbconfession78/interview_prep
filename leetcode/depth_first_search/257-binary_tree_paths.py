# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        return self.helper(root, "", [])

    def helper(self, root, lst_str, retlist):
        if root:
            if root.left is None and root.right is None:
                retlist.append(lst_str+str(root.val))

            if root.left:
                self.helper(root.left, lst_str + str(root.val) +'->', retlist)

            if root.right:
                self.helper(root.right, lst_str + str(root.val) + '->', retlist)

        return retlist



def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(6)
    print(Solution().binaryTreePaths(root))

    root = None
    print(Solution().binaryTreePaths(root))


if __name__ == '__main__':
    main()

# Intructions:
"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \   /  \
  5 2    6
All root-to-leaf paths are:

["1->2->5", "1->3"]
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""
