#!/usr/bin/python3
from tree_node import Node
from binary_tree import *
import sys

def main():
    tree = BinarySearchTree()
    """
    data = [7, 1, 2, 3, 4, 5, 6, 8]
    data = [1, 2, 5, 3, 6, 4]
    t = 6
    for i in range(t):
        x = data[i]
        tree.create(x)
    """
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
  
    top_view(tree.root)


def top_view(root):
    get_left_view(root)
    sys.stdout.write('{} '.format(root.data))
    get_right_view(root)

def get_left_view(root):
    if root.left is None:
        return root

    get_left_view(root.left)
    sys.stdout.write('{} '.format(root.left.data))

def get_right_view(root):
    if root.right is None:
        return root

    sys.stdout.write('{} '.format(root.right.data))
    get_right_view(root.right)

        
if __name__ == '__main__':
    main()
