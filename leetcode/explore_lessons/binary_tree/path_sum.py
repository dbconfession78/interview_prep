from data_structures.binary_tree import *
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        def helper(root, tot):
            if root.left is None and root.right is None:
                val = 0
                if root.val:
                    val = root.val
                if tot + val == sum:
                    return True
                return False

            val = 0
            if root.val:
                val = root.val
            tot += val
            if root.left and helper(root.left, tot):
                return True
            if root.right and helper(root.right, tot):
                return True
            return False

        if root is None or root.val is None:
            return False
        return helper(root, 0)


def main():
    # T
    print(Solution().hasPathSum(build_binary_tree([5,4,8,11,None,13,4,7,2,None,None,None,1]), 22))

    # F
    print(Solution().hasPathSum(build_binary_tree([5,4,8,11,None,13,4,7,2,None,None,None,1]), 21))

    # F
    print(Solution().hasPathSum(build_binary_tree([]), 0))

    # F
    print(Solution().hasPathSum(build_binary_tree([1,2]), 1))



# LC input
# [5,4,8,11,null,13,4,7,2,null,null,null,1]
# 22
# [5,4,8,11,null,13,4,7,2,null,null,null,1]
# 21
# []
# 0
# [1,2]
# 1

if __name__ == '__main__':
    main()