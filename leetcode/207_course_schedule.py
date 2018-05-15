"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) == 1:
            return True
        if prerequisites == []:
            return True
        dct = {}
        for req in prerequisites:
            dct[req[0]] = req[1]

        for elem in prerequisites:
            req = elem[1]
            seen = set()
            seen.add(elem[0])
            while req is not None:
                if req not in dct:
                    break
                if req in seen:
                    return False
                seen.add(req)
                req = dct.get(req)
        return True

def main():
    print(Solution().canFinish(2, [[1,0]])) # True
    print(Solution().canFinish(2, [[1,0],[0,1]]))   # False
    print(Solution().canFinish(1, []))    # True
    print(Solution().canFinish(3, [[1,0],[1,2],[0,1]])) # False
    print(Solution().canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]])) # False
    print(Solution().canFinish(2, [[1,0]])) # True
    print(Solution().canFinish(3, [[1,0]])) # True
    print(Solution().canFinish(3, [[1,0],[2,0]])) # True

# LC input
# 2
# [[1,0]]
# 2
#  [[1,0],[0,1]]
# 1
# []
# 3
# [[1,0],[1,2],[0,1]]
# 4
# [[2,0],[1,0],[3,1],[3,2],[1,3]]
# 2
# [[1,0]]
# 3
# [[1,0]]
# 3
# [[1,0],[2,0]]
if __name__ == '__main__':
    main()