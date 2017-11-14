#!/usr/bin/python3
import sys

class Node:
    def __init__(self,data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

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

def add_right(data, parent):
    parent.right = Node(data)
    return parent

def add_left(data, parent):
    parent.left = Node(data)
    return parent

def in_order(root):
    if root is not None:
        in_order(root.left)
        sys.stdout.write('{} '.format(root.data))
        in_order(root.right)
    return root

def pre_order(root):
    if root is not None:
        sys.stdout.write(str(root.data))
        sys.stdout.write(' ')
        pre_order(root.left)
        pre_order(root.right)
    return root

def post_order(root):
    if root is not None:
        post_order(root.left)
        post_order(root.right)
        sys.stdout.write('{} '.format(root.data))

    return root
