class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    # def inorderTraversal_STK(self, root):
    def levelOrder(self, root):
        if root is None:
            return root
        stk = [[root]]
        retval = []
        while stk:
            row = stk.pop()
            if row:
                _len = len(row)
                i = 0
                nums = []
                lvl = []
                while i < _len:
                    node = row[i]
                    nums.append(node.val)

                    for child in node.left, node.right:
                        if child:
                            lvl.append(child)
                    i += 1
                if lvl:
                    stk.append(lvl)
                if nums:
                    retval.append(nums)
        return retval



def main():
    # root = Node(3)
    # root.left = Node(9)
    # root.right = Node(20)
    # root.right.left = Node(15)
    # root.right.right = Node(7)
    # print(Solution().levelOrder(root))   #
    #
    # root = None
    # print(Solution().levelOrder(root))  #

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(Solution().levelOrder(root))


# LC input
# [1,2,3,4,5]
if __name__ == '__main__':
    main()