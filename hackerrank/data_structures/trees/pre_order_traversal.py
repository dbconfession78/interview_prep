#!/usr/bin/python3
from tree_node import Node
from binary_tree import *
import sys

def main():
    root = Node(data=1)
    root = add_right(2, root)
    root.right = add_right(5, root.right)
    root.right.right = add_right(6, root.right.right)
    root.right.right = add_left(3, root.right.right)
    root.right.right.left = add_right(4, root.right.right.left)

    pre_order(root)
    print()
def pre_order(root):
    if root is not None:
        sys.stdout.write(str(root.data))
        sys.stdout.write(' ')
        pre_order(root.left)
        pre_order(root.right)
    return root











if __name__ == '__main__':
    main()
