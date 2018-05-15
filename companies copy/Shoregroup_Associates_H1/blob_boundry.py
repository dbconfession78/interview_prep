"""
Boundary Challenge
A Blob is a shape in two-dimensional integer coordinate space where all cells have at least one adjoining cell to the right, left, top, or bottom that is also occupied. Given a 10x10 array of boolean values that represents a Blob uniformly selected at random from the set of all possible Blobs that could occupy that array, write a program that will determine the Blob boundaries. Optimize for finding the correct result, performing a minimum number of cell Boolean value reads, and elegance and clarity of the solution.

Sample input: (Please view in a monospaced font)
0000000000
0011100000
0011111000
0010001000
0011111000
0000101000
0000101000
0000111000
0000000000
0000000000

Sample output:
Cell Reads: 44
Top: 1
Left: 2
Bottom: 7
Right: 6
"""
test_no = 1

class BoundaryFinder:
    def __init__(self):
        self.reads = 0
        self.seen = set()
        self.bounds = {"top": float('inf'), "left": float("inf"), "bottom": 0, "right": 0}
        self.done = False

    def blob_boundry(self, arr):
        def helper(arr, i, j):
            if (i,j) in self.seen or i < 0 or i > len(arr)-1 or j < 0 or j > len(arr[i])-1:
                return

            self.reads += 1
            self.seen.add((i, j))
            if arr[i][j] == 0:
                return

            self.bounds["top"] = min(self.bounds["top"], i)
            self.bounds["left"] = min(self.bounds["left"], j)
            self.bounds["bottom"] = max(self.bounds["bottom"], i)
            self.bounds["right"] = max(self.bounds["right"], j)
            helper(arr, i - 1, j)
            helper(arr, i, j - 1)
            helper(arr, i + 1, j)
            helper(arr, i, j + 1)

        for i in range(10):
            if self.done: break
            for j in range(10):
                if arr[i][j] == 1:
                    helper(arr, i, j)
                    self.done = True
                    break
                else:
                    self.reads += 1
                    self.seen.add((i, j))

        print("\nCell Reads: {}\nTop: {}\nLeft: {}\nBottom: {}\nRight: {}".format(self.reads, self.bounds["top"], self.bounds["left"], self.bounds["bottom"], self.bounds["right"]))

        return self.bounds


def blob_boundry_WITH_START(arr, i, j, dct, dir):
# def blob_boundry(arr, i, j, dct, dir):
    global reads
    def helper(arr, i, j, dct, dir):
        global reads
        if i >= 0 and i < len(arr)-1 and j >= 0 and j < len(arr)-1:
            print(arr[i][j])
        if arr[i][j] == -1:
            return dct
        reads += 1
        if i < 0 or i > len(arr)-1 or j < 0 or j > len(arr[i])-1 or arr[i][j] == 0:
            if dir == "U":
                dct[dir] = min(dct[dir], i + 1)
            elif dir == "L":
                dct[dir] = min(dct[dir], j + 1)
            elif dir == "R":
                dct[dir] = max(dct[dir], j - 1)
            elif dir == "D":
                dct[dir] = max(dct[dir], i - 1)
            return dct

        arr[i][j] = -1
        dct = helper(arr, i-1, j, dct, "U")
        dct = helper(arr, i, j-1, dct, "L")
        dct = helper(arr, i+1, j, dct, "D")
        dct = helper(arr, i, j+1, dct, "R")
        return dct

    # dct = helper(arr, i, j, dct, dir) # <--- for use with other version
    dct = helper(arr, i, j, dct, dir)
    print(dct)
    print(reads)
    print()


def test(sol, retval):
    global test_no
    print("{}. ".format(test_no), end="")
    test_no += 1
    if retval != sol:
        print("FAIL", end=" ")
    else:
        print("OK", end=" ")
    print(" - sol: {},  ret: {}".format(sol, retval))


def main():
    ######### TESTS ############
    print(BoundaryFinder().blob_boundry([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]))

    print(BoundaryFinder().blob_boundry([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]))

if __name__ == "__main__":
    main()

