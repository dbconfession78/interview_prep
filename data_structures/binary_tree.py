#!/usr/bin/python3
from data_structures.binary_search_tree import BST_node
import sys


class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None  
        self.right = None 
        self.level = None
        self.parent = None
        # self.next = None

    def __str__(self):
        return str(self.val)


class BinaryTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root is None:
            self.root = TreeNode(val)
        else:
            current = self.root
         
            while True:
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = TreeNode(val)
                        break
                elif val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        current.right = TreeNode(val)
                        break
                else:
                    break

    def add_left(self, val):
        new = TreeNode(val)

        walk = self.root
        while walk:
            if walk.left is None:
                new.parent = walk
                walk.left = new
                return
            walk = walk.left

    def get_height(self):
        def helper(root):
            if root is None:
                return -1

            left = get_height(root.left) + 1
            right = get_height(root.right) + 1
            return max(left, right)

        return helper(self.root)


def build_binary_tree(lst):
    """
    builds iteratively from lst in level-order (breadth first) fashion
    """
    if not lst:
        return TreeNode(None)
    root = TreeNode(lst.pop(0))
    stk = [[root]]
    while stk:
        row = stk.pop(0)
        row_len = len(row)
        i = 0
        while i < row_len:
            node = row.pop(0)
            if lst:
                if type(lst[0]) is TreeNode:
                    node.left = lst.pop(0)
                else:
                    node.left = TreeNode(lst.pop(0))
                row.append(node.left)
            else:
                break
            if lst:
                if type(lst[0]) is TreeNode:
                    node.right = lst.pop(0)
                else:
                    node.right = TreeNode(lst.pop(0))
                row.append(node.right)
            else:
                break
            i += 1
        if row:
            stk.append(row)
    return root


def connect(root):
    """
    connects each node with the node to it's right
    """
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


def print_nexts(root):
    """
    prints the 'val' stored in the node to the right of each node
    """
    stk = [[root]]
    while stk:
        row = stk.pop()
        row_len = len(row)
        i = 0
        while i < row_len:
            node = row.pop(0)
            s = f"{str(node.val)} -> "
            s += str(node.next.val) if node.next else "None"
            print(s)
            for child in node.left, node.right:
                if child:
                    row.append(child)
            i += 1
        if row:
            stk.append(row)
    print()


def get_height(root):
    if root is None:
        return -1

    left = get_height(root.left) + 1
    right = get_height(root.right) + 1
    return max(left, right)


def is_balanced(root):
    def helper(root):
        if root is None or root == []:
            return 0
        l_height = helper(root.left)
        if l_height == -1:
            return -1
        r_height = helper(root.right)
        if r_height == -1:
            return -1
        if abs(l_height - r_height) >1:
            return -1
        return max(l_height, r_height) + 1

    if helper(root) < 0:
        return False
    return True_


def top_view(root):
    get_left_view(root)
    sys.stdout.write('{} '.format(root.val))
    get_right_view(root)


def get_left_view(root):
    if root.left is None:
        return root

    get_left_view(root.left)
    sys.stdout.write('{} '.format(root.left.val))


def get_right_view(root):
    if root.right is None:
        return root

    sys.stdout.write('{} '.format(root.right.val))
    get_right_view(root.right)


def add_right(val, parent):
    parent.right = TreeNode(val)
    return parent


def add_left(val, parent):
    parent.left = TreeNode(val)
    return parent


def in_order(root):
    if root is not None:
        in_order(root.left)
        sys.stdout.write('{} '.format(root.val))
        in_order(root.right)
    return root


def pre_order(root):
    if root is not None:
        sys.stdout.write(str(root.val))
        sys.stdout.write(' ')
        pre_order(root.left)
        pre_order(root.right)
    return root


def post_order(root):
    if root is not None:
        post_order(root.left)
        post_order(root.right)
        sys.stdout.write('{} '.format(root.val))

    return root


def print_binary_tree(root):
    """
    :return: list of integer lists, each representing a subsequent BT row.
    :NOTE:  None implies TreeNode(None). 'null' implies there isn't a node present
    """
    if root is None:
        print("['_']")
        return
    stk = [[root]]
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
                if type(node) is TreeNode or type(node) is BST_node:
                    nums.append(node.val)

                    for child in node.left, node.right:
                        if child:
                            child_row_empty = False
                            lvl.append(child)
                        else:
                            lvl.append("_")
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


def levelOrder(root):
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


def is_symmetric(root):
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
    T = build_binary_tree([2,None,3,1])
    print_binary_tree(T)

    T = build_binary_tree([1,2,2,3,4,4,3,5,6,7,8,8,7,6,5])
    print()


if __name__ == "__main__":
    main()
