#!/usr/bin/python3
from tree_node import Node
from binary_tree import *
import sys

height = 0
def main():
    tree = BinarySearchTree()
    t = 7
    nodes = [3,5,2,1,4,6,7]
    for i in range(t):
        x = nodes[i]
        tree.create(x)

    print(height(tree.root))
    
def height(root):
    height = get_height(root, 0)
    return height

def get_height(root, height):
    l_height = 0
    r_height = 0
    if root == None or (root.left == None and root.right == None):
        return height

    l_height = get_height(root.left, height + 1)
    r_height = get_height(root.right, height + 1)
    if l_height > r_height:
        return l_height
    else:
        return r_height
        
if __name__ == '__main__':
    main()
