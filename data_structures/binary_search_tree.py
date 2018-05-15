import math
import traceback
class BST_node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self, root=None):
        self.root = root
        self.size = 0
        self.row_count = 0
        self.row_lim = 1
        self.next_lim = 2

    def insert(self, val):
        new = BST_node(val)
        if self.root is None:
            self.root = new
            self.row_count = 1
            self.size = 1
            return

        def dfs(node):
            try:
                if new.val == node.val:
                    error = "Cannot insert duplicate values"
                    raise Exception(error)
            except:
                print(traceback.format_exc())
                return -1

            if new.val < node.val:
                if node.left is None:
                    node.left = new
                    return 0
                else:
                    if dfs(node.left) == -1:
                        return -1
            else:
                if node.right is None:
                    node.right = new
                else:
                    if dfs(node.right) == -1:
                        return -1
            return 0

        if dfs(self.root) == -1:
            return -1
        self.size += 1
        self.row_count = int(math.sqrt(self.size))+1


    def search(self, val):
        def helper(node):
            if node is None:
                return False
            if helper(node.left):
                return True
            if node.val == val:
                return True
            if helper(node.right):
                return True
            return False

        return helper(self.root)

    def print_bst(self):
        """
        :return: list of integer lists, each representing a subsequent BT row.
        :NOTE:  None implies TreeNode(None). 'null' implies there isn't a node present
        """
        if self.root is None:
            return self.root
        stk = [[self.root]]
        retval = []
        while stk:
            child_row_empty = True
            row = stk.pop()
            if row:
                _len = len(row)
                i = 0
                nums = []
                lvl = []
                while i < _len:
                    node = row[i]
                    if type(node) is BST_node:
                        nums.append(node.val)

                        for child in node.left, node.right:
                            if child:
                                child_row_empty = False
                                lvl.append(child)
                            else:
                                lvl.append('_')
                    else:
                        nums.append('_')
                    i += 1
                if child_row_empty:
                    lvl = []

                if lvl:
                    stk.append(lvl)
                if nums:
                    retval.append(nums)
        print(retval)

    def print_bst_layered(self):
        """
        attempts to print a visually accurate BST
        :return:
        """
        stk = [self.root]
        row_num = 0
        while stk:
            row_num += 1
            stk_len = len(stk)
            output_row = []
            i = 0
            while i < stk_len:
                node = stk.pop(0)
                output_row.append(node.val if node else None)
                if node:
                    for child in (node.left, node.right):
                            stk.append(child)
                i += 1
            if any([x is not None for x in output_row]):
                print('\t' * ((self.row_count) - row_num) + '{}'.format(output_row))


def build_bst(lst):
    def helper(lst):
        if not lst:
            return None

        _len = len(lst)

        if _len == 1:
            return BST_node(lst[0])

        mid_i = _len // 2
        mid_v = lst[mid_i]
        node = BST_node(mid_v)
        left_lst = lst[0:mid_i]
        right_lst = lst[mid_i + 1:]
        node.left = helper(left_lst)
        node.right = helper(right_lst)
        return node

    nones_lst = [i for i, elem in enumerate(lst) if elem is None]

    if nones_lst:
        lst = [x for x in lst if x]
    lst.sort()
    if nones_lst:
        for idx in nones_lst:
            lst.insert(idx, None)
    root = helper(lst)
    bst = BST(root)

    return bst

# def build_bst_TO_DEL(lst):
#
#     bst = BST()
#     failed = []
#     for n in lst:
#         if bst.insert(n) == -1:
#             failed.append(n)
#     if failed:
#         print("The following duplicate values were not inserted to the BST: {}".format(failed))
#     return bst


def main():
    bst = build_bst([236,104,701,227,911,30])
    bst.print_bst()


if __name__ == '__main__':
    main()
