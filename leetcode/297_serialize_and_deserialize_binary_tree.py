# Instructions
"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""


import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def __init__(self):
        self.data = None
        self.root = None
        self.node_pos = 0


    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == []:
            return ''
        self.data = '{}:'.format(root.val)
        stk = [[root.left, root.right]]
        while stk:
            children = stk.pop()
            for child in children:
                if child:
                    self.data += '{}:'.format(child.val)
                    stk.insert(0, ([child.left, child.right]))
                else:
                    self.data += 'null:'
        return self.data


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.replace('null', 'None')


        data = data.split(':')
        if data == ['']:
            return None
        root = TreeNode(int(data.pop(0)))
        n_stk = [root]
        while data and n_stk:
            node = n_stk.pop()

            x = data.pop(0)
            if x != 'None':
                node.left = TreeNode(int(x))
            x = data.pop(0)
            if x != 'None':
                node.right = TreeNode(int(x))

            if node.right:
                n_stk.append(node.right)
            if node.left:
                n_stk.append(node.left)

        return root





    def prepare_data(self, data):
        data = data.replace('null', 'None')
        self.data = data.split(':')



    def get_ser_str(self):
        return self.data


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

    def print_tree(self, root):
        print('TREE')
        def helper(root):
            if root is None:
                sys.stdout.write('null, ')
                return

            sys.stdout.write('{}, '.format(root.val))
            helper(root.left)
            helper(root.right)

        sys.stdout.write('[')
        helper(root)
        print(']')





def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()
    codec.print_tree(codec.deserialize(codec.serialize(root)))

    root = []
    codec = Codec()
    codec.print_tree(codec.deserialize(codec.serialize(root)))

    # # codec = Codec()
    # # data1 = codec.serialize(root)
    # # codec = Codec()
    # # root2 = codec.deserialize(data1)
    #
    # codec = Codec()
    # data2 = codec.serialize(root2)
    # print(data1 == data2)
    #
    #
    # codec = Codec()
    # codec.deserialize(codec.serialize(root))





if __name__ == '__main__':
    main()
