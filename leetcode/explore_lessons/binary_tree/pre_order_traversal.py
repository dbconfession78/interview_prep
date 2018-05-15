class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    # def preorderTraversal_STK(self, roo):
    def preorderTraversal(self, root):
        stk = [root]
        retlst = []
        while stk:
            top = stk.pop()
            if top:
                retlst.append(top.val)
                if top.right:
                    stk.append(top.right)
                if top.left:
                    stk.append(top.left)
        return retlst

    def preorderTraversal_REC(self, root):
    # def preorderTraversal(self, root):
        return self.helper(root, [])

    def helper(self, root, retlst):
        if root is None:
            return retlst

        retlst.append(root.val)
        self.helper(root.left, retlst)
        self.helper(root.right, retlst)
        return retlst


def main():
    root = Node(1)
    root.right = Node(2)
    root.right.left = Node(3)
    print(Solution().preorderTraversal(root))   # [1, 2, 3]


if __name__ == '__main__':
    main()