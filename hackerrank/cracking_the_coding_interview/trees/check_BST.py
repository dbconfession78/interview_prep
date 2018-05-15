import sys
import cProfile
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.origin_data = None

def main():
    root = node(16)
    # 4
    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 16 18 19 20 21 22 23 24 25 26 27 28 29 30 31

    root.left = node(8)
    root.left.left = node(4)

    root.left.left.left = node(2)
    root.left.left.left.left = node(1)
    root.left.left.left.right = node(3)

    root.left.left.right = node(6)
    root.left.left.right.left = node(5)
    root.left.left.right.right = node(7)

    root.left.right = node(12)

    root.left.right.left = node(10)
    root.left.right.left.left = node(9)
    root.left.right.left.right = node(11)

    root.left.right.right = node(14)
    root.left.right.right.left = node(13)
    root.left.right.right.right = node(15)

    root.right = node(24)

    root.right.left = node(20)
    root.right.left.left = node(18)
    root.right.left.left.left = node(17)

    root.right.left.right = node(22)
    root.right.left.right.left = node(21)
    root.right.left.right.right = node(23)

    root.right.right = node(28)
    root.right.right.left = node(26)
    root.right.right.left.left = node(25)
    root.right.right.left.right = node(27)

    root.right.right.right= node(30)
    root.right.right.right.left = node(29)
    root.right.right.right.right = node(31)







    print(checkBST(root))


def is_bst(root, min, max):
    if root is None:
        # print(True)
        return True

    if min and root.data <= min:
        # print(root.data)
        # print(False)
        return False

    if max and root.data >= max:
        # print(root.data)
        # print(False)
        return False
    ret = is_bst(root.left, min, root.data) and is_bst(root.right, root.data, max)
    # print(root.data)
    # print(ret)
    return ret


def checkBST(root):
    return is_bst(root, None, None)




if __name__ == '__main__':
    main()
    # cProfile.run('main()')
