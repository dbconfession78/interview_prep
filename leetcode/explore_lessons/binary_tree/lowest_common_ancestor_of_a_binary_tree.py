"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the
lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since
a node can be a descendant of itself according to the LCA definition.
"""
from data_structures.binary_tree import *


class Solution(object):
    # def lowestCommonAncestor_PRACTICE(self, root, p, q):
    def lowestCommonAncestor(self, root, p, q):
        return

    def lowestCommonAncestor_PASSED(self, root, p, q):
    # def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stk = [(root, [])]
        tgt_ancestors = []
        while stk:
            row = stk.pop()
            row_len = len(row)
            i = 0
            while i < row_len:
                node, ancestors = row.pop(0)
                if node == p or node == q:
                    tgt_ancestors.append(ancestors)
                    if len(tgt_ancestors) == 2:
                        if p in tgt_ancestors[0] or p in tgt_ancestors[1]:
                            return p
                        if q in tgt_ancestors[0] or q in tgt_ancestors[1]:
                            return q
                        retval = None
                        while tgt_ancestors[0] and tgt_ancestors[1]:
                            a = tgt_ancestors[0].pop(0)
                            b = tgt_ancestors[1].pop(0)
                            if a == b:
                                retval = a
                        return tgt_ancestors[0][0] if retval is None else retval
                for child in node.left, node.right:
                    if child:
                        row.append((child, ancestors + [node]))
                i += 1
            if row:
                stk.append(row)


def main():
    p = TreeNode(5)
    q = TreeNode(1)
    print(Solution().lowestCommonAncestor(
        build_binary_tree([3,p,q,6,2,0,8,None,None,7,4,None,None,None,None]),
        p,
        q))

    p = TreeNode(5)
    q = TreeNode(4)
    print(Solution().lowestCommonAncestor(
        build_binary_tree([3,p,1,6,2,0,8,None,None,7,q,None,None,None,None]),
        p,
        q))


    """
        -1
       /  \
      0    3
    /  \
   -2   4
   /
   8 
    """
    p = TreeNode(8)
    q = TreeNode(4)
    print(Solution().lowestCommonAncestor(
        build_binary_tree([-1,0,3,-2,q,None,None,p]),
        p,
        q))


if __name__ == '__main__':
    main()

