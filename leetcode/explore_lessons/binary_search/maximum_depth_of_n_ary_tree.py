"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:

            1
        /   |   \
      3     2    4
    /   \          \
   5     6          8
          \          \
           7           9
                      /  \
                    10   11
                            \
                            12


We should return its max depth, which is 6.

Note:
The depth of the tree is at most 1000.
The total number of nodes is at most 5000.

"""


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        stk = [([root], 0)]
        retval = 0
        while stk:
            row, curr_h = stk.pop()
            retval = max(retval, curr_h)
            row_len = len(row)
            i = 0
            if row:
                while i < row_len:
                    node = row.pop(0)
                    for child in node.children:
                        if child:
                            row.append(child)
                    i += 1
                stk.append((row, curr_h+1))
        return retval


def main():
    root1 = Node(1, [])
    n1 = Node(3, [])
    n2 = Node(2, [])
    n3 = Node(4, [])
    n4 = Node(5, [])
    n5 = Node(6, [])
    n6 = Node(7, [])
    n7 = Node(8, [])
    n8 = Node(9, [])
    n9 = Node(10, [])
    n10 = Node(11, [])
    n11 = Node(12, [])

    root1.children += [n1, n2, n3]
    n1.children += [n4, n5]
    n3.children += [n7]
    n5.children += [n6]
    n7.children += [n8]
    n8.children += [n9, n10]
    n10.children += [n11]

    print(Solution().maxDepth(root1))


if __name__ == '__main__':
    main()
