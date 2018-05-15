from data_structures.binary_tree import *
def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    # def is_symmetric_PRACTICE(self, root):
    def is_symmetric(self, root):
        return

    def is_sym(self, row):
        row_len = len(row)
        if row_len % 2 != 0:
            return False
        for i in range(row_len // 2):
            l = row[i].val
            r = row[-i-1].val
            if row[i].val != row[-i-1].val:
                return False
        return True

    def is_symmetric_PASSED(self, root):
    # def is_symmetric(self, root):
        if root is None:
            return True
        stk = [[root]]
        while stk:
            row = stk.pop()
            row_len = len(row)
            mid_i = row_len // 2
            next = []
            for node in row:
                if node:
                    for child in node.left, node.right:
                        # if child:
                        next.append(child)
                    left_nodes = row[0:mid_i][::-1]
                    right_nodes = row[mid_i:]
                    for i, x in enumerate(left_nodes):
                        l_val = x if x else None
                        r_val = right_nodes[i].val if right_nodes[i] else None
                        if l_val != r_val:
                            return False
            row = next
            if row:
                stk.append(row)
        return True


def main():
    # print(Solution().is_symmetric(build_binary_tree([])))               # T
    print(Solution().is_symmetric(build_binary_tree([1,2,2,3,4,4,3])))  # T
    print(Solution().is_symmetric(build_binary_tree([1,2,6,3,4,4,3])))  # F

    # T
    print(Solution().is_symmetric(build_binary_tree([1,2,2,3,4,4,3,5,6,7,8,8,7,6,5])))

    # F
    print(Solution().is_symmetric(build_binary_tree([1,2,2,None,3,None,3])))


# LC input
# []
# [1,2,2,3,4,4,3]
# [1,2,6,3,4,4,3]
# [1,2,2,3,4,4,3,5,6,7,8,8,7,6,5]
# [1,2,2,null,3,null,3]
if __name__ == '__main__':
    main()