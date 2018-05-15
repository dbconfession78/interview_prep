# Definition for binary tree:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None
# from data_structures.binary_tree import *
def hasPathWithGivenSum(t, s):
    def helper(t, s, tot):
        if t is None:
            return True if tot == s else False

        if helper(t["left"], s, tot+t["value"]):
            return True

        if helper(t["right"], s, tot+ t["value"]):
            return True
        return False


    if t and t["value"] == s:
        if (t["left"] or t["right"]):
            return False
        return True
    return helper(t, s, 0)

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
    "value": 4,
    "left": {
        "value": 1,
        "left": {
            "value": -2,
            "left": None,
            "right": {
                "value": 3,
                "left": None,
                "right": None
            }
        },
        "right": None
    },
    "right": {
        "value": 3,
        "left": {
            "value": 1,
            "left": None,
            "right": None
        },
        "right": {
            "value": 2,
            "left": {
                "value": -2,
                "left": None,
                "right": None
            },
            "right": {
                "value": -3,
                "left": None,
                "right": None
            }
        }
    }
}
    retval = hasPathWithGivenSum(t, 7)
    test(retval, True)

    t = {
        "value": 4,
        "left": {
            "value": 1,
            "left": {
                "value": -2,
                "left": None,
                "right": {
                    "value": 3,
                    "left": None,
                    "right": None
                }
            },
            "right": None
        },
        "right": {
            "value": 3,
            "left": {
                "value": 1,
                "left": None,
                "right": None
            },
            "right": {
                "value": 2,
                "left": {
                    "value": -4,
                    "left": None,
                    "right": None
                },
                "right": {
                    "value": -3,
                    "left": None,
                    "right": None
                }
            }
        }
    }
    retval = hasPathWithGivenSum(t, 7)
    test(retval, False)

    t = None
    retval = hasPathWithGivenSum(t, 0)
    test(retval, True)

    t = None
    retval = hasPathWithGivenSum(t, 1)
    test(retval, False)

    t = {
    "value": 5,
    "left": None,
    "right": None
    }
    retval = hasPathWithGivenSum(t, 5)
    test(retval, True)

    t = {
    "value": 5,
    "left": None,
    "right": None
    }
    retval = hasPathWithGivenSum(t, -5)
    test(retval, False)

    t = {
    "value": 5,
    "left": None,
    "right": None
    }
    retval = hasPathWithGivenSum(t, 0)
    test(retval, False)

    t = {
    "value": 8,
    "left": None,
    "right": {
        "value": 3,
        "left": None,
        "right": None
    }
}
    retval = hasPathWithGivenSum(t, 8)
    test(retval, False)


if __name__ == '__main__':
    main()