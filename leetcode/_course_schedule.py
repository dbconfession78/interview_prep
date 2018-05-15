class Solution(object):
    def canFinish_PRACTICE(self, numCourses, prerequisites):
    # def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    # def canFinish_MINE(self, numCourses, prerequisites):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]

        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True



def main():
    print(Solution().canFinish(2, [[1, 0]]))    # True
    print(Solution().canFinish(3, [[1, 0]]))    # True
    print(Solution().canFinish(2, [[0, 1]]))    # True

# LC input
# 2
# [[1,0]]
# 3
# [[1,0]]
# 2
# [[0,1]]

if __name__ == '__main__':
    main()