"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.


click to show more hints.

Hints:

This problem is equivalent to finding the topological order in a directed graph. If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.
"""
from collections import defaultdict
import collections


class Solution:
    def __init__(self, sol):
        self.sol = sol

    # def findOrder_2(self, numCourses, prerequisites):
    def findOrder(self, numCourses, prerequisites):
        dct = {i: set() for i in range(numCourses)}
        neighbors = defaultdict(set)
        for i, j in prerequisites:
            dct[i].add(j)
            neighbors[j].add(i)

        q = [x for x in dct.keys() if not dct[x] ]
        count, res = 0, []
        while q:
            node = q.pop(0)
            res.append(node)
            count += 1
            for i in neighbors[node]:
                dct[i].remove(node)
                if not dct[i]:
                    q.append(i)
        if count == numCourses:
            return res
        return []




    def findOrder_1(self, numCourses, prerequisites):
    # def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        dct1 = defaultdict(list)
        dependencies = defaultdict(list)
        retval = []
        next_len = 1
        seen = set()
        course_set = set()
        for i, elem in enumerate(prerequisites[::-1]):
            course_set.add(elem[0])
            dct1[elem[0]].append(elem[1])
            dependencies[elem[1]].append(elem[0])

        if not dct1:
            return [x for x in range(numCourses)]
        stk = [max(dct1.items())]
        while stk:
            _len = next_len
            next_len = 0
            i = 0
            while i < _len:
                course_number, neighbors = stk.pop(0)
                if course_number not in seen:
                    retval.append(course_number)
                    if course_number in course_set:
                        course_set.remove(course_number)
                seen.add(course_number)
                if neighbors:
                    for neigh in neighbors:
                        if course_number in dct1[neigh]:
                            return []
                        if neigh not in seen:
                            k = neigh
                            v = dct1.get(k)
                            stk.append((k, v))
                            next_len += 1

                i += 1
        retval = retval[::-1]
        # course_lst = sorted(list(course_set))

        # while course_lst:
        #     retval.append(course_lst.pop())
        # _len = len(retval)
        if _len < numCourses:
            return []
        return retval
        # while _len < numCourses:
        #     retval.insert(0, _len)
        #     _len += 1
        #
        # return retval


    def test(self, retval):
        if retval != self.sol:
            print("FAIL: ")
            print(f"retval: {retval}")
            print(f"expected: {self.sol}")
            return -1
        print("OK")
        return 0


def main():
    # sol = Solution([0,1])
    # retval = sol.findOrder(2, [[1,0]])
    # sol.test(retval)
    #
    # sol = Solution([0])
    # retval = sol.findOrder(1, [])
    # sol.test(retval)
    #
    # sol = Solution([0, 1])
    # retval = sol.findOrder(2, [])
    # sol.test(retval)
    #
    # sol = Solution([0,1,2,3])
    # retval = sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    # sol.test(retval)
    #
    # sol = Solution([1,0])
    # retval = sol.findOrder(2, [[0,1]])
    # sol.test(retval)
    #
    # sol = Solution([])
    # retval = sol.findOrder(2, [[0,1],[1,0]])
    # sol.test(retval)

    sol = Solution([2,0,1])
    retval = sol.findOrder(3, [[1,0]])
    sol.test(retval)

    sol = Solution([0,2,1])
    retval = sol.findOrder(3, [[1,0],[2,0]])
    sol.test(retval)

    sol = Solution([])
    retval = sol.findOrder(3, [[1,0],[0,2],[2,1]])
    sol.test(retval)



# LC Input
# 2
# [[1,0]]
# 1
# []
# 2
# []
# 4
# [[1,0],[2,0],[3,1],[3,2]]
# 2
# [[0,1],[1,0]
# 3
# [[1,0]]
# 3
# [[1,0],[2,0]]
# 3
# [[1,0],[0,2],[2,1]]

if __name__ == '__main__':
    main()