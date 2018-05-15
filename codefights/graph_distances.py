"""
You have a connected directed graph that has positive weights in the adjacency matrix g. The graph is represented as a
square matrix, where g[i][j] is the weight of the edge (i, j), or -1 if there is no such edge.

Given g and the index of a start vertex s, find the minimal distances between the start vertex s and each of the
vertices of the graph.

Example

For

g = [[-1, 3, 2],
     [2, -1, 0],
     [-1, 0, -1]]

and s = 0, the output should be
graphDistances(g, s) = [0, 2, 2].

Example

    The distance from the start vertex 0 to itself is 0.
    The distance from the start vertex 0 to vertex 1 is 2 + 0 = 2.
    The distance from the start vertex 0 to vertex 2 is 2.

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.array.integer g

    The graph is represented as a square matrix, as described above.

    Guaranteed constraints:
    1 ≤ g.length ≤ 100,
    g.length = g[i].length,
    -1 ≤ g[i][j] ≤ 30.

    [input] integer s

    The start vertex (0-based).

    Guaranteed constraints:
    0 ≤ s < g.length.

    [output] array.integer

    An array, the ith element of which is equal to the distance between the start vertex s and the ith vertex of the
    graph g.
"""
test_no = 1
import sys
from collections import defaultdict
def print_graph(g):
    for r in g:
        print(r)


# def graphDistances_1(g, s):
def graphDistances(g, s):
    print_graph(g)
    retval = []
    if len(g) == 1 and len(g[0]) == 0:
        return [0,0,0]
    for i in range(len(g)):
        tmp_lst = []
        if i == s:
            retval.append(0)
        else:
            seen = defaultdict(set)
            # seen = {x:set() for x in range(len(g))}
            stk = [[s, (seen, g[s], 0)]]
            mn = float('inf')

            dct = {}
            while stk:
                idx, rest = stk.pop(0)
                seen = rest[0]
                row = rest[1]
                dist = rest[2]
                # seen.add(idx)
                for j, elem in enumerate(row):
                    if idx == s:
                        dist = 0
                        # seen = set()
                    # if (idx, j) not in seen:

                    if j not in seen:
                        seen[idx].add(j)
                        # print("adding: ({},{})".format(idx, j))
                        # seen.add((idx, j))
                        if elem > -1:
                            if j == i:
                                tmp_lst.append(dist + elem)
                                mn = min(mn, dist + elem)
                            else:
                                new_dist = dist + elem
                                stk.insert(0, [j, (seen, g[j], new_dist)])
                    else:
                        print("skipping: ({}, {})".format(idx, j))
                print()
            retval.append(mn)
    return retval


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
    # test([0, 2, 2], graphDistances([[-1, 3, 2],
    #                                 [2, -1, 0],
    #                                 [-1, 0, -1]], 0))
    #
    # test([0, 0, 2], graphDistances([[-1,1,2],
    #                                 [0,-1,3],
    #                                 [0,0,-1]], 1))

    test([4, 3, 1, 10, 0, 4, 1, 1, 0, 4], graphDistances([
        [-1, -1, 19, 8, 18, -1, -1, -1, -1, -1],
        [10,  6,  4, 7,  0, 10, 18, -1,  0, -1],
        [-1, -1, 15,-1, 17,  3, -1, 14, 16,  3],
        [ 4, 19,  3,15,  8,  4,  6, 11,  5,  8],
        [ 5,  3, 10,-1,  0, 14, 15,  1, 16,  5],
        [-1,  8, -1,-1,  5, -1,  5,  0,  1, -1],
        [-1, 18, -1,19,  2, -1, 10, -1,  8,  6],
        [14,  8, 12,16, -1, -1,  0, 16, 15, 17],
        [4,   5,  1,12,  0,  4,  8, 15,  1, -1],
        [13,  7, 17,-1,  4, 13, 16,  3, 12,  9]], 8))


if __name__ == "__main__":
    main()
