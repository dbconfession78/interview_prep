# Instructions
"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
"""


class Solution:
    # def nextClosestTime_NEW(self, time):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nums = list(sorted(set([ord(x)-48 for x in time if x != ':'])))
        H1 = [x for x in nums if x <= 2]
        H1.append(H1[0])

        H2 = []
        if (ord(time[0])-48) == 2:
            H2 = [x for x in nums if x < 4]
            H2.append(H2[0])
        else:
            for elem in nums:
                H2.append(elem)

        H2.append(H2[0])

        M1 = [x for x in nums if x <= 5]
        M1.append(M1[0])

        M2 = [x for x in nums]
        M2.append(M2[0])

        new = time
        m2_last_val = ord(time[4]) - 48
        M2_i = M2.index(m2_last_val)
        m2_next_val = M2[M2_i+1]
        new = new[0:4] + str(m2_next_val)

        m1_next_val = m1_last_val = ord(new[3]) - 48
        m2_over = False
        if m2_next_val < m2_last_val:
            m2_over = True
            M1_i = M1.index(m1_last_val)
            m1_next_val = M1[M1_i+1]
            new = new[0:3] + str(m1_next_val) + new[4]

        h2_next_val = h2_last_val = ord(new[1]) - 48
        m1_over = False
        if m1_next_val < m1_last_val or (m2_over and new[3] == time[3]):
            m1_over = True
            H2_i = H2.index(h2_last_val)
            h2_next_val = H2[H2_i+1]
            new = new[0:1] + str(h2_next_val) + new[2:]

        if h2_next_val < h2_last_val or (m1_over and new[1] == time[1]):
            h1_last_val = ord(time[0]) - 48
            H1_i = H1.index(h1_last_val)
            h1_next_val = H1[H1_i+1]
            new = str(h1_next_val) + new[1:]
        return new

    def nextClosestTime_OLD(self, time):
    # def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nums = list(sorted(set([ord(x)-48 for x in time if x != ':'])))
        H1 = [x for x in nums if x <= 2]
        H1.append(H1[0])

        H2 = []

        for elem in nums:
            H2.append(elem)

        H2.append(H2[0])

        M1 = [x for x in nums if x <= 5]
        M1.append(M1[0])

        M2 = [x for x in nums]
        M2.append(M2[0])

        new = time
        m2_last_val = ord(time[4]) - 48
        M2_i = M2.index(m2_last_val)
        m2_next_val = M2[M2_i+1]
        new = new[0:4] + str(m2_next_val)

        m1_next_val = ord(new[3]) - 48
        m1_last_val = ord(new[3]) - 48
        m2_over = False
        if m2_next_val < m2_last_val:
            m2_over = True
            m1_last_val = ord(time[3]) - 48
            M1_i = M1.index(m1_last_val)
            m1_next_val = M1[M1_i+1]
            new  = new[0:3] + str(m1_next_val) + new[4]

        if (ord(time[0])-48) == 2:
            H2 = [x for x in nums if x < 4]
            H2.append(H2[0])

        h2_next_val = ord(new[1]) - 48
        h2_last_val = ord(new[1]) - 48
        m1_over = False
        if m1_next_val < m1_last_val or (m2_over and new[3] == time[3]):
            m1_over = True
            h2_last_val = ord(time[1]) - 48
            H2_i = H2.index(h2_last_val)
            h2_next_val = H2[H2_i+1]
            new = new[0:1] + str(h2_next_val) + new[2:]

        if h2_next_val < h2_last_val or (m1_over and new[1] == time[1]):
            h1_last_val = ord(time[0]) - 48
            H1_i = H1.index(h1_last_val)
            h1_next_val = H1[H1_i+1]
            new = str(h1_next_val) + new[1:]
        return new

def main():
    print(Solution().nextClosestTime("19:34"))  # "19:39"
    print(Solution().nextClosestTime("23:59"))  # "22:22"
    print(Solution().nextClosestTime("16:27"))  # "17:11"
    print(Solution().nextClosestTime("21:13"))  # "21:21"
    print(Solution().nextClosestTime("18:04"))  # "18:08"
    print(Solution().nextClosestTime("12:52"))  # "12:55"
    print(Solution().nextClosestTime("01:14"))  # "01:40"
    print(Solution().nextClosestTime("17:39"))  # "19:11"
    print(Solution().nextClosestTime("16:18"))  # "18:11"


# LC input
# "19:34"
# "23:59"
# "16:27"
# "21:13"
# "18:04"
# "12:52"
# "01:14"
# "17:39"
# "16:18"

if __name__ == '__main__':
    main()