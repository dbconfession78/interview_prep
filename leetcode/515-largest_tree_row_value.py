# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # fastest version
    def largestValues3(self, root):
        row = [root]
        bigs = []
        while any(row):
            bigs.append(max(x.val for x in row))
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        return bigs

    # same speed as fastest, just has list comprehension expanded
    def largestValues(self, root):
        if root is None:
            return []
        row = [root]
        bigs = []
        while row:
            row_big = None
            for elem in row:
                val = elem.val
                if row_big is None:
                    row_big = val
                else:
                    row_big = max(row_big, val)
            bigs.append(row_big)

            row_len = len(row)
            i = 0
            next_row = []
            while i < row_len:
                for kid in (row[i].left, row[i].right):
                    if kid:
                        next_row.append(kid)
                i += 1
            row = next_row
        return bigs

    # slowest version
    def largestValues2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        q = [root]
        bigs = []

        while q:
            row_len = len(q)
            i = 0
            row_big = None
            while i < row_len:
                top = q[0]
                q = q[1:]
                if row_big is None:
                    row_big = top.val
                else:
                    row_big = max(row_big, top.val)
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
                i += 1
            bigs.append(row_big)
        return bigs



def main():
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right = TreeNode(2)
    root.right.right = TreeNode(9)

    # root.left.left.left = TreeNode(11)
    # root.left.left.right = TreeNode(17)
    # root.left.right.left= TreeNode(22)
    # root.left.right.right= TreeNode(16)

    # root.right.right.left = TreeNode(5)
    # root.right.right.right = TreeNode(50)

    print(Solution().largestValues(root))


if __name__ == '__main__':
    main()

# Instructions
"""
You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]

"""