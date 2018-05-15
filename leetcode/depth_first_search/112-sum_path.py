
# Instructions
"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        return self.helper2(root, 0, sum)

    def helper2(self, root, tot, tgt):
        if not root.left and not root.right:
            tot += root.val
            return tot == tgt

        if root.left:
            if self.helper2(root.left, tot + root.val, tgt):
                return True
        if root.right:
            if self.helper2(root.right, tot + root.val, tgt):
                return True
        return False

    # uses recursion
    def hasPathSum_REC(self, root, sum):
    # def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if sum in self.check_path(root, 0, []):
            return True
        return False

    def check_path(self, root, tot, sums):
        if root.left is None and root.right is None:
            sums.append(tot + root.val)
        else:
            if root.left:
                self.check_path(root.left, tot+root.val, sums)
            if root.right:
                self.check_path(root.right, tot+root.val, sums)
        return sums

    # using stack
    def hasPathSum_STK(self, root, sum):
    # def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        stack = [root]
        seen = []
        current_sum = 0
        while stack:
            x = stack.pop()
            current_sum += x.val
            # print(current_sum)
            if current_sum == sum and x.left is None and x.right is None:
                return True
            if x.left:
                seen.append({'idx': x, 's': current_sum})
            if current_sum > sum and stack:
                current_sum = seen.pop().get('s')
                continue
            for node in (x.left, x.right):
                if node:
                    stack.append(node)

            if x.left is None and x.right is None:
                if seen:
                    current_sum = seen.pop().get('s')
        return False


def main():
    root = None
    print(Solution().hasPathSum(root, 1))   # False

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print(Solution().hasPathSum(root, 22))  # True

    root = TreeNode(1)
    print(Solution().hasPathSum(root, 1))   # True

    root = TreeNode(1)
    print(Solution().hasPathSum(root, 0))  # False

    root = TreeNode(1)
    root.left = TreeNode(2)
    print(Solution().hasPathSum(root, 1))  # False

    root = TreeNode(-2)
    root.right = TreeNode(-3)
    print(Solution().hasPathSum(root, -5))  # True

    root = TreeNode(1)
    root.right = TreeNode(1)
    root.left = TreeNode(21)
    root.left.left = TreeNode(1)
    print(Solution().hasPathSum(root, 22))  # False

#LC input
# []
# 1
# [5,4,8,11,null,13, 4,7,2,null, null, null, 1]
# 22
# [1]
# 1
# [1]
# 0
# [1,2]
# 1
# [-2,null,-3]
# -5
# [1,21,1,1]
# 22


if __name__ == '__main__':
    main()


