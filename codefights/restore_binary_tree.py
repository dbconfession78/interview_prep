
# Definition for binary tree:
class Tree(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

from data_structures.binary_tree import print_binary_tree, levelOrder
def restoreBinaryTree(inorder, preorder):
    if inorder:
        idx = inorder.index(preorder.pop(0))
        root = Tree(inorder[idx])

        root.left = restoreBinaryTree(inorder[:idx], preorder)
        root.right = restoreBinaryTree(inorder[idx+1:], preorder)
        return root

def test(retval, sol):
    if retval != sol:
        print("FAIL: ")
        print(f"retval: {retval}")
        print(f"expected: {sol}")
        return -1
    print("OK")
    return 0


def main():
    root = restoreBinaryTree([4, 2, 1, 5, 3, 6], [1, 2, 4, 3, 5, 6])
    print(levelOrder(root))




if __name__ == '__main__':
    main()

