# Meeting Rooms
"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine
if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.
"""
from bisect import bisect


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    # def canAttendMeetings_PRACTICE(self, intervals):
    def canAttendMeetings(self, intervals):
        return

    def canAttendMeetings_PASSED(self, intervals):
        # def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        next_end = None
        ends = []
        intervals = sorted(intervals, key=lambda k: k.start)
        for i, inter in enumerate(intervals):
            start = inter.start
            end = inter.end

            if next_end:
                if start < next_end:
                    return False
            if ends:
                ends.pop(0)
            ends.insert(bisect(ends, end), end)
            next_end = ends[0]
        return True


def main():
    print(Solution().canAttendMeetings([]))  # True

    print(Solution().canAttendMeetings([Interval(0, 30),
                                        Interval(5, 10),
                                        Interval(15, 20)]))  # False

    print(Solution().canAttendMeetings([Interval(7, 10),
                                        Interval(2, 4)]))  # True

    print(Solution().canAttendMeetings([Interval(1, 5),
                                        Interval(8, 9)]))  # True

    print(Solution().canAttendMeetings([Interval(5, 8),
                                        Interval(6, 8)]))  # False

    print(Solution().canAttendMeetings([Interval(2, 7)]))  # True

    print(Solution().canAttendMeetings([Interval(13, 15),
                                        Interval(1, 13)]))  # True

    print(Solution().canAttendMeetings([Interval(1, 5),
                                        Interval(8, 9),
                                        Interval(8, 9)]))  # False

    print(Solution().canAttendMeetings([Interval(1, 8),
                                        Interval(6, 20),
                                        Interval(9, 16),
                                        Interval(13, 17)]))  # False

    print(Solution().canAttendMeetings([Interval(2, 36),
                                        Interval(3, 4),
                                        Interval(13, 34),
                                        Interval(16, 20),
                                        Interval(39, 46)]))  # False

    print(Solution().canAttendMeetings([Interval(765, 989),
                                        Interval(466, 472),
                                        Interval(860, 996),
                                        Interval(338, 932),
                                        Interval(618, 639),
                                        Interval(616, 936),
                                        Interval(832, 864),
                                        Interval(92, 758)]))  # False


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
