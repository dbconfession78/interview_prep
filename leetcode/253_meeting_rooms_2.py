# Meeting Rooms 2
"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
"""

from bisect import bisect
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # def minMeetingRooms_PRACTICE(self, intervals):
    def minMeetingRooms(self, intervals):
        return

    # 250ms
    def minMeetingRooms_PASSED(self, intervals):
    # def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda k: (k.start))

        running = 0
        ends = []
        next_end = float('inf')
        for i, inter in enumerate(intervals):
            if inter.start < next_end:
                running += 1
            if inter.start >= next_end:
                ends.pop(0)
            ends.insert(bisect(ends, inter.end), inter.end)
            next_end = ends[0]
        return running


def main():
    print(Solution().minMeetingRooms([]))                   # 0

    print(Solution().minMeetingRooms([Interval(0,30),
                                      Interval(5,10),
                                      Interval(15,20)]))    # 2

    print(Solution().minMeetingRooms([Interval(7,10),
                                      Interval(2,4)]))      # 1

    print(Solution().minMeetingRooms([Interval(1,5),
                                      Interval(8,9)]))      # 1

    print(Solution().minMeetingRooms([Interval(5,8),
                                      Interval(6,8)]))      # 2

    print(Solution().minMeetingRooms([Interval(2,7)]))      # 1

    print(Solution().minMeetingRooms([Interval(13, 15),
                                      Interval(1, 13)]))    # 1

    print(Solution().minMeetingRooms([Interval(1, 5),
                                      Interval(8, 9),
                                      Interval(8, 9)]))     # 2

    print(Solution().minMeetingRooms([Interval(1, 8),
                                      Interval(6, 20),
                                      Interval(9, 16),
                                      Interval(13, 17)]))   # 3

    print(Solution().minMeetingRooms([Interval(2, 36),
                                      Interval(3, 4),
                                      Interval(13, 34),
                                      Interval(16, 20),
                                      Interval(39, 46)]))   # 3

    print(Solution().minMeetingRooms([Interval(765, 989),
                                      Interval(466, 472),
                                      Interval(860, 996),
                                      Interval(338, 932),
                                      Interval(618, 639),
                                      Interval(616, 936),
                                      Interval(832, 864),
                                      Interval(92, 758)]))  # 5


# LC input
# []
# [[0,30],[5,10],[15,20]]
# [[7,10],[2,4]]
# [[1,5],[8,9]]
# [[5,8],[6,8]]
# [[2,7]]
# [[13,15],[1,13]]
# [[1,5],[8,9],[8,9]]
# [[1,8],[6,20],[9,16],[13,17]]
# [[2,36],[3,4],[13,34],[16,20],[39,46]]
# [[765,989],[466,472],[860,996],[338,932],[618,639],[616,936],[832,864],[92,758]]
if __name__ == '__main__':
    main()