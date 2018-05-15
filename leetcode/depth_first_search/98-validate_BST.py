# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None or root == [] or root.val is None:
            return True

        stk = []
        walk = root
        pre = None
        while walk or stk:
            if walk:
                stk.append(walk)
                walk = walk.left
            else:
                p = stk.pop()
                if pre and p.val <= pre.val:
                    return False
                else:
                    pre = p
                    walk = p.right
        return True




def main():
    """Test cases"""
    # case 1
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(Solution().isValidBST(root))

    # case 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().isValidBST(root))

    # case
    root = TreeNode(None)
    print(Solution().isValidBST(root))

    # case
    root = TreeNode(100)
    root.left = TreeNode(50)
    root.left.left = TreeNode(40)
    root.left.right = TreeNode(55)
    root.left.left.left = TreeNode(30)
    root.left.left.right = TreeNode(45)
    root.left.right.left = TreeNode(54)
    root.left.right.right = TreeNode(56)

    root.right = TreeNode(200)
    root.right.left = TreeNode(150)
    root.right.right = TreeNode(250)

    root.right.left.left = TreeNode(140)
    root.right.left.right = TreeNode(155)
    root.right.right.left = TreeNode(240)
    root.right.right.right = TreeNode(255)
    print(Solution().isValidBST(root))

    # case
    root = TreeNode(1)
    root.left = TreeNode(1)
    print(Solution().isValidBST(root))

    # case
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(20)
    print(Solution().isValidBST(root))



if __name__ == '__main__':
    main()

# Instructions
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