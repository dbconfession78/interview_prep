# Instructions
"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # def kthSmallest_PRACTICE(self, root, k):
    def kthSmallest(self, root, k):
        return



    def kthSmallest_LC(self, root, k):
    # def kthSmallest(self, root, k):
        def helper(root, vals):
            if root is None:
                return
            if len(vals) == k:
                return
            helper(root.left, vals)
            vals.append(root.val)
            helper(root.right, vals)

        vals = []
        helper(root, vals)
        return vals[k-1]

    count = None
    retval = None
    first_leaf = False
    should_grab = False

    def kthSmallest_WITH_KRISTEN(self, root, k):
    # def kthSmallest(self, root, k):
        global count, retval, first_leaf, should_grab
        self.count = None
        self.retval = None
        self.helper(root, k)
        return self.retval

    def helper(self, root, k):
        global count, retval, first_leaf, should_grab

        if root is None:
            if self.first_leaf is False:
                self.count = k
                self.first_leaf = True
            return

        self.helper(root.left, k)
        self.count -= 1
        if self.count <= 0:
            if not self.retval:
                self.retval = root.val
            return
        self.helper(root.right, k)
        if self.count <= 0:
            return


def main():
    root = TreeNode(100)
    root.left = TreeNode(90)
    root.left.left = TreeNode(80)
    root.left.right= TreeNode(95)
    root.right = TreeNode(200)
    root.right.left = TreeNode(150)
    root.right.right = TreeNode(300)
    print(Solution().kthSmallest(root, 1)) # 80
    print(Solution().kthSmallest(root, 2)) # 90
    print(Solution().kthSmallest(root, 3)) # 95
    print(Solution().kthSmallest(root, 4)) # 100
    print(Solution().kthSmallest(root, 5))   # 150
    print(Solution().kthSmallest(root, 6)) # 200
    print(Solution().kthSmallest(root, 7)) # 300


if __name__ == '__main__':
    main()


# plan -> keys:
# keys -> debug (first submit):
# debug -> accepted:
# Total
