#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def kthSmallestInBST(t, k):
    def helper(t, k, lst):
        if t is None:
            return lst

        lst = helper(t.left, k, lst)
        lst.append(t.value)
        lst = helper(t.right, k, lst)
        return lst

    return helper(t, k, [])[::-1][k - 1]




