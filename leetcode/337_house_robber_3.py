# 337. House Robber III
"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob_PRACTICE(self, root):
    # def rob(self, root):
        return

    # def rob_PASSED(self, root):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return root

        stk1 = [root]
        stk2 = []
        retval = 0
        row_sums = [root.val]
        rows = [[root.val]]
        while stk1:
            _this = stk1
            stk1 = []
            for node in _this:
                for x in (node.left, node.right):
                    if x:
                        stk2.append(x)
            rows.append([x.val for x in stk2])
            money = sum([x.val for x in stk2])
            row_sums.append(money)
            stk1 += stk2
            stk2 = []
            retval = max(retval, money)

        print(rows)
        sum_even_rows = sum([x for i, x in enumerate(row_sums) if i % 2 == 0])

        sum_odd_rows = sum([x for i, x in enumerate(row_sums) if i % 2 != 0])
        return max(sum_even_rows, sum_odd_rows)





def main():
    """
         3
        / \
       2   3
        \   \
         3   1
    """
    # root = TreeNode(3)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.right = TreeNode(3)
    # root.right.right = TreeNode(1)
    # print(Solution().rob(root))
    #
    # """
    #      3
    #     / \
    #    4   5
    #   / \   \
    #  1   3   1
    # """
    # root = TreeNode(3)
    # root.left = TreeNode(4)
    # root.right = TreeNode(5)
    # root.left.left = TreeNode(1)
    # root.left.right = TreeNode(3)
    # root.right.right = TreeNode(1)
    # print(Solution().rob(root))


    """
             4
            / 
           1   
          / 
         2 
        /
       3 
    """
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.left.left = TreeNode(2)
    root.left.left.left = TreeNode(3)
    print(Solution().rob(root))

# LC Input
# [3,2,3,null,3,null,1]
# [1,2,3,null,4, null, 5]
# [1, 2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# []
# [4,1,null,2,null,3]
# [4,2,null,1,3]

# * [1-15] input is not represented in this files test cases yet. it's output should be 97

if __name__ == '__main__':
    main()

