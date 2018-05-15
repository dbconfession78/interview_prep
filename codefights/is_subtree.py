#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isSubtree(t1, t2):
    def helper(t1, t2):
        if t1 is None:
            return False

        if helper(t1["left"], t2):
            return True
        if t2["value"] == t1["value"]:
            w2 = t2
            if check_tree(t1, w2):
                return True
        if helper(t1["right"], t2):
            return True
        return False

    def check_tree(t1, t2):
        if t1 is None and t2 is None:
            return True

        if not t1 or not t2:
            return False
        if check_tree(t1["left"], t2["left"]) == False:
            return False
        if t1["value"] != t2["value"]:
            return False
        if check_tree(t1["right"], t2["right"]) == False:
            return False
        return True

    return helper(t1, t2)

def test(retval, sol):
    if retval != sol:
        print("FAIL: ")
        print(f"retval: {retval}")
        print(f"expected: {sol}")
        return -1
    print("OK")
    return 0

def main():
    t1 = {
        "value": 5,
        "left": {
            "value": 10,
            "left": {
                "value": 4,
                "left": {
                    "value": 1,
                    "left": None,
                    "right": None
                },
                "right": {
                    "value": 2,
                    "left": None,
                    "right": None
                }
            },
            "right": {
                "value": 6,
                "left": None,
                "right": {
                    "value": -1,
                    "left": None,
                    "right": None
                }
            }
        },
        "right": {
            "value": 7,
            "left": None,
            "right": None
        }
    }
    t2 = {
        "value": 10,
        "left": {
            "value": 4,
            "left": {
                "value": 1,
                "left": None,
                "right": None
            },
            "right": {
                "value": 2,
                "left": None,
                "right": None
            }
        },
        "right": {
            "value": 6,
            "left": None,
            "right": {
                "value": -1,
                "left": None,
                "right": None
            }
        }
    }
    retval = isSubtree(t1, t2)
    test(retval, True)

    t1 = {
        "value": 5,
        "left": {
            "value": 10,
            "left": {
                "value": 4,
                "left": {
                    "value": 1,
                    "left": None,
                    "right": None
                },
                "right": {
                    "value": 2,
                    "left": None,
                    "right": None
                }
            },
            "right": {
                "value": 6,
                "left": {
                    "value": -1,
                    "left": None,
                    "right": None
                },
                "right": None
            }
        },
        "right": {
            "value": 7,
            "left": None,
            "right": None
        }
    }
    t2 = {
        "value": 10,
        "left": {
            "value": 4,
            "left": {
                "value": 1,
                "left": None,
                "right": None
            },
            "right": {
                "value": 2,
                "left": None,
                "right": None
            }
        },
        "right": {
            "value": 6,
            "left": None,
            "right": {
                "value": -1,
                "left": None,
                "right": None
            }
        }
    }


    retval = isSubtree(t1, t2)
    test(retval, False)


if __name__ == '__main__':
    main()
    
"""
    def helper(t1, t2):
        if t1 is None:
            return False

        if helper(t1.left, t2):
            return True
        if t2.value == t1.value:
            w2 = t2
            if check_tree(t1, w2):
                return True
        if helper(t1.right, t2):
            return True
        return False

    def check_tree(t1, t2):
        if t1 is None and t2 is None:
            return True

        if check_tree(t1.left, t2.left) == False:
            return False
        if t1.value != t2.value:
            return False
        if check_tree(t1.right, t2.right) == False:
            return False
        return True

    return helper(t1, t2)
    """