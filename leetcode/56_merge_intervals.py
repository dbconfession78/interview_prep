# 56. Merge Intervals
"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
from bisect import bisect


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # def merge_PRACTICE(self, intervals):
    def merge(self, intervals):
        return



    # 186 ms
    def merge_PASSED(self, intervals):
    # def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        _len = len(intervals)
        i = 0

        intervals = sorted(intervals, key=lambda k: k.start)
        retlst  = []
        while i < _len:
            if not retlst:
                retlst.append([intervals[i].start, intervals[i].end])
            else:
                if intervals[i].start >= retlst[-1][0] and intervals[i].start <= retlst[-1][1]:
                    merge = [None, None]
                    merge[0] = retlst[-1][0]
                    merge[1] = max(intervals[i].end, retlst[-1][1])
                    retlst.pop()
                    retlst.append(merge)
                else:
                    retlst.append([intervals[i].start, intervals[i].end])
            i += 1
        return retlst



def main():
    # print(Solution().merge([Interval(1,3),
    #                         Interval(2,6),
    #                         Interval(8,10),
    #                         Interval(15,18)]))  # [1,6],[8,10],[15,18]
    #
    # print(Solution().merge([Interval(1,4),
    #                         Interval(4,5)]))    # [[1,5]]
    #
    # print(Solution().merge([Interval(1,4),
    #                         Interval(2,3)]))    # [[1,4]]
    #
    # print(Solution().merge([Interval(1,4),
    #                         Interval(0,2),
    #                         Interval(3,5)]))    # [[0,5]]

    print(Solution().merge([Interval(4,5),
                            Interval(1,4),
                            Interval(0,1)]))      # [[0,5]]


# LC input
# [[1,3],[2,6],[8,10],[15,18]]
# [[1,4],[4,5]]
# [[1,4],[2,3]]
# [[1,4],[0,2],[3,5]]
# [[4,5],[1,4],[0,1]]


if __name__ == '__main__':
    main()
