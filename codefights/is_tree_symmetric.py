"""
Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.

Example

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": {
            "value": 3,
            "left": None,
            "right": None
        },
        "right": {
            "value": 4,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 2,
        "left": {
            "value": 4,
            "left": None,
            "right": None
        },
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    }
}
the output should be isTreeSymmetric(t) = true.

Here's what the tree in this example looks like:

    1
   / \
  2   2
 / \ / \
3  4 4  3
As you can see, it is symmetric.

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": None,
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 2,
        "left": None,
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    }
}
the output should be isTreeSymmetric(t) = false.

Here's what the tree in this example looks like:

    1
   / \
  2   2
   \   \
   3    3
As you can see, it is not symmetric.
"""


#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isTreeSymmetric(t):
    if not t:
        return True
    stk = [[t]]
    while stk:
        row = stk.pop()
        new_row = []
        _len = len(row)
        if _len > 1:
            left = [x["value"] if x else None for x in row[:_len // 2]]
            right = [x["value"] if x else None for x in row[_len // 2:]]
            if left != right[::-1]:
                return False
        i = 0
        while i < _len:
            node = row[i]
            if node:
                for child in node["left"], node["right"]:
                    if child:
                        new_row.append(child)
                    else:
                        new_row.append(None)
            i += 1
        if new_row:
            stk.append(new_row)
    return True

def test(retval, sol):
    if retval != sol:
        print("FAIL: ")
        print(f"retval: {retval}")
        print(f"expected: {sol}")
        return -1
    print("OK")
    return 0

def main():
    t = {
        "value": 1,
        "left": {
            "value": 2,
            "left": {
                "value": 3,
                "left": None,
                "right": None
            },
            "right": {
                "value": 4,
                "left": None,
                "right": None
            }
        },
        "right": {
            "value": 2,
            "left": {
                "value": 4,
                "left": None,
                "right": None
            },
            "right": {
                "value": 3,
                "left": None,
                "right": None
            }
        }
    }
    retval = isTreeSymmetric(t)
    test(retval, True)

    t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": None,
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": 2,
        "left": None,
        "right": {
            "value": 3,
            "left": None,
            "right": None
        }
    }
}
    retval = isTreeSymmetric(t)
    test(retval, False)

    


if __name__ == '__main__':
    main()
