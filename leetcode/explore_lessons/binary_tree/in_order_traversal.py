class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    # def inorderTraversal_STK(self, root):
    def inorderTraversal(self, root):
        stk = [root]
        retlst = []
        while stk:
            top = stk.pop()
            if top:
                if top.right is None:
                    if top.left:
                        retlst.append(top.left.val)
                        retlst.append(top.val)
                    else:
                        retlst.append(top.val)
                else:
                    retlst.append(top.val)
                    stk.append(top.right)
        return retlst

    def inorderTraversal_REC(self, root):
    # def inorderTraversal(self, root):
        return self.helper(root, [])

    def helper(self, root, retlst):
        if root is None:
            return retlst

        self.helper(root.left, retlst)
        retlst.append(root.val)
        self.helper(root.right, retlst)
        return retlst


def main():
    root = Node(1)
    root.right = Node(2)
    root.right.left = Node(3)

    print(Solution().inorderTraversal(root))   # [1, 3, 2]

if __name__ == '__main__':
    main()