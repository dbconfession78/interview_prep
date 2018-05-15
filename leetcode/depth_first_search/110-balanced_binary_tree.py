# from data_structures.binary_tree import get_height
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def isBalanced_PRACTICE(self, root):
    def isBalanced(self, root):
        return


    def isBalanced_PASSED(self, root):
    # def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(root):
            if root is None or root == []:
                return 0
            l_height = helper(root.left)
            if l_height == -1:
                return -1
            r_height = helper(root.right)
            if r_height == -1:
                return -1

            if abs(l_height - r_height) > 1:
                return -1
            return 1 + max(l_height, r_height)

        ret = helper(root)
        if ret < 0:
            return False
        return True


def main():
    # case 0
    # root = [] # True
    #
    # # case 1
    # root = TreeNode(1)
    # print(Solution().isBalanced(root))    # True
    #
    # # case 2
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # print(Solution().isBalanced(root))    # True

    # case 3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(61)
    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    root.left.left.right.right = TreeNode(80)
    root.left.left.right.left = TreeNode(60)
    root.right.left = TreeNode(8)
    root.right.left.right = TreeNode(9)
    root.right.right = TreeNode(10)
    root.right.right.left = TreeNode(-5)
    root.right.right.right = TreeNode(11)
    root.right.right.right.right = TreeNode(12)
    root.right.right.right.left = TreeNode(13)
    print(Solution().isBalanced(root))  # True

    # case 4
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.left.left = TreeNode(1)
    root.left.left.left.left = TreeNode(1)
    root.left.left.left.left.left = TreeNode(1)
    root.left.left.left.left.left.left = TreeNode(1)
    print(Solution().isBalanced(root))  # False

    # case 5
    root = TreeNode(1)
    root.right = TreeNode(1)
    root.right.right = TreeNode(1)
    root.right.right.right = TreeNode(1)
    print(Solution().isBalanced(root))  # False

    # case 6
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.right.right = TreeNode(20)
    root.right.right.right= TreeNode(15)
    print(Solution().isBalanced(root))    # False

    # case 7
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    print(Solution().isBalanced(root))  # True


#LC input
# []
# [1]
# [1,1]
# [1,2,3,4,5,8,10,6,7,null,61,null,9,5,11,null,null,60,80, null,null,null,null,null,null,13,12]
# [1,1,null,1,null,1,null,1,null,1,null,1]
# [1,null,1,null,1,null,1,null]
# [1,2,2,3,null,null,3,4,null,null,4]
# [1,1,1]



if __name__ == '__main__':
    main()

# Instructions:
"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

"""