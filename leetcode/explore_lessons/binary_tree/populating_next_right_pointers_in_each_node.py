"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be
set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two
children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""
from data_structures.binary_tree import build_binary_tree, print_nexts


class Solution:
    def connect(self, root):
        if root is None or root.val is None:
            return
        stk = [[root]]
        while stk:
            row = stk.pop()
            row_len = len(row)
            i = 0
            while i < row_len:
                node = row.pop(0)
                if i < row_len-1:
                    node.next = row[0]
                for child in node.left, node.right:
                    if child:
                        row.append(child)
                i += 1
            if row:
                stk.append(row)


def main():
    root = build_binary_tree([1, 2, 3, 4, 5, 6, 7])
    Solution().connect(root)
    print_nexts(root)

    root = build_binary_tree([])
    Solution().connect(root)
    print_nexts(root)


if __name__ == '__main__':
    main()
