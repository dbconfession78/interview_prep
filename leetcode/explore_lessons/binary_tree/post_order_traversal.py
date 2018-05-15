class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # def postorderTraversal_STK(self, root):
    def postorderTraversal(self, root):
        stk = [root]
        retval = []
        while stk:
            top = stk.pop()
            if top:
                for child in (top.left, top.right):
                    if child:
                        stk.append(child)
                retval.insert(0, top.val)
        return retval

    def postorderTraversal_REC(self, root):
    # def postorderTraversal(self, root):
        return self.helper(root, [])

    def helper(self, root, retval):
        if root is None:
            return retval
        self.helper(root.left, retval)
        self.helper(root.right, retval)
        retval.append(root.val)
        return retval


def main():
    root = Node(1)
    root.right = Node(2)
    root.right.left = Node(3)

    print(Solution().postorderTraversal(root))   # [3, 2, 1]

if __name__ == '__main__':
    main()