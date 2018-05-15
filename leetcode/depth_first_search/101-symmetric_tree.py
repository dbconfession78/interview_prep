# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None or root == []:
            return True
        q = [root]
        while q:
            row_len = len(q)
            for i in range(row_len):
                top = q[i]
                if top is not None:
                    for child in (top.left, top.right):
                        q.append(child)

            current = q[:row_len]
            while current:
                front = current[0]
                end = current[len(current) - 1]
                if (front is None and end is not None) or (front is not None and end is None):
                    return False
                if front is not None and end is not None:
                    if front.val != end.val:
                       return False
                current = current[1:]
                if current:
                    current.pop()
            q = q[row_len:]
        return True









def main():
    # case 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(Solution().isSymmetric(root))

    # case 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)

    print(Solution().isSymmetric(root))


def build_height_bal_BST(arr):
    if arr == []:
        return None
    mid_idx = len(arr) // 2
    root = TreeNode(arr[mid_idx])
    root.left = build_height_bal_BST(arr[:mid_idx])
    root.right = build_height_bal_BST(arr[mid_idx+1:])
    return root

if __name__ == '__main__':
    main()


# Instructions:
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""