"""
Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
Explanation:
The first two events can be booked.  The third event can be double booked.
The fourth event (5, 15) can't be booked, because it would result in a triple booking.
The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
"""

from data_structures.binary_search_tree import *
from data_structures.binary_search_tree import build_bst
class Booking:
    def __init__(self, start, end, db):
        self.start = start
        self.end = end
        self.db = db


class MyCalendarTwo(object):
    def __init__(self):
        self.bookings = []
        self.overlaps = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, b in enumerate(self.bookings):
            if start > b.start and end <= b.end:
                self.overlaps.append()


def main():
    # mc = MyCalendarTwo()
    # b = [10,20],[50,60],[10,40],[5,15],[5,10],[25,55]
    # for x in b:
    #     print(mc.book(x[0], x[1]))

    mc = MyCalendarTwo()
    b = [24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]
    for i, x in enumerate(b):
        print(mc.book(x[0], x[1]))
    # [null,true,true,true,true,false,false,true,false,false,false]






# LC input
# ["MyCalendarTwo","book","book","book","book","book","book"]
# [[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
# ["MyCalendarTwo","book","book","book","book","book","book","book","book","book","book"]
# [[],[24,40],[43,50],[27,43],[5,21],[30,40],[14,29],[3,19],[3,14],[25,39],[6,19]]


if __name__ == '__main__':
    main()

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)