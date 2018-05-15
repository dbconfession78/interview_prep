# 261 Task Scheduler
"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""

from collections import Counter
from collections import defaultdict
import operator
class Solution:
    # def leastInterval_PRACTICE(self, tasks, n):
    def leastInterval(self, tasks, n):
       return


    def leastInterval_PASSED(self, tasks, n):
    # def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        _map = [0 for x in range(26)]
        retval = 0
        for c in tasks:
            _map[ord(c) - ord('A')] += 1

        _map.sort()
        while _map[25] > 0:
            i = 0
            while i <= n:
                if _map[25] == 0:
                    break
                if i < 26 and _map[25 - i] > 0:
                    _map[25 - i] -= 1
                i += 1
                retval += 1
            _map.sort()
        return retval




def main():
    print(Solution().leastInterval(["A","A","A","B","B","B"], 2))   # 8
    print(Solution().leastInterval(["A","A","A","B","B","B"], 0))   # 6
    print(Solution().leastInterval(["A","A","A","B","B","B"], 50))  # 104
    print(Solution().leastInterval(["A","A","A","B","B","B"], 10))  # 24
    print(Solution().leastInterval(["A","A","A","B","B","B"], 4))   # 12
    print(Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))   # 16
    print(Solution().leastInterval(["A","A","A","A","A","A","B","B","B","B","C","C","C","C","D","D","D","E","E","E","F","F","G","G"], 2))  # 24
    print(Solution().leastInterval(["A","B","C","D","E","A","B","C","D","E"], 4))  # 10


# LC input
# ["A","A","A","B","B","B"]
# 2
# ["A","A","A","B","B","B"]
# 0
# ["A","A","A","B","B","B"]
# 50
# ["A","A","A","B","B","B"]
# 10
# ["A","A","A","B","B","B"]
# 4
# ["A","A","A","A","A","A","B","C","D","E","F","G"]
# 2
# ["A","A","A","A","A","A","B","B","B","B","C","C","C","C","D","D","D","E","E","E","F","F","G","G"]
# 2
# ["A","B","C","D","E","A","B","C","D","E"]
# 4

if __name__ == '__main__':
    main()
