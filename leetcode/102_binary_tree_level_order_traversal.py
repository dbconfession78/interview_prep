# Instructions
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        retlst = []
        if root is None:
            return retlst
        stk = [root]

        while stk:
            _len = len(stk)
            lvl = []
            for i in range(_len):
                _this = stk.pop(0)
                lvl.append(_this.val)
                for x in (_this.left, _this.right):
                    if x:
                        stk.append(x)
            retlst.append(lvl)
        return retlst

def print_solution(lst):
    for row in lst:
        print(row)

def main():
    root  = None
    print_solution(Solution().levelOrder(root))

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)
    print_solution(Solution().levelOrder(root))

# LC input
# []
#

if __name__ == '__main__':
    main()