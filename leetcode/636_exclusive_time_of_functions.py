# Instructions
"""
Given the running logs of n functions that are executed in a nonpreemptive single threaded CPU, find the exclusive time of these functions.

Each function has a unique id, start from 0 to n-1. A function may be called recursively or by another function.

A log is a string has this format : function_id:start_or_end:timestamp. For example, "0:start:0" means function 0 starts from the very beginning of time 0. "0:end:0" means function 0 ends to the very end of time 0.

Exclusive time of a function is defined as the time spent within this function, the time spent by calling other functions should not be considered as this function's exclusive time. You should return the exclusive time of each function sorted by their function id.


Example
==============
Input:

n = 2
logs =
["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]

Output:[3, 4]
==============

Explanation:
Function 0 starts at time 0, then it executes 2 units of time and reaches the end of time 1.
Now function 0 calls function 1, function 1 starts at time 2, executes 4 units of time and end at time 5.
Function 0 is running again at time 6, and also end at the time 6, thus executes 1 unit of time.
So function 0 totally execute 2 + 1 = 3 units of time, and function 1 totally execute 4 units of time.

Note:
1. Input logs will be sorted by timestamp, NOT log id.
2. Your output should be sorted by function id, which means the 0th element of your output corresponds to the exclusive time of function 0.
3. Two functions won't start or end at the same time.
4. Functions could be called recursively, and will always end.
5. 1 <= n <= 100
"""


class Solution(object):
    def exclusiveTime_PRACTICE(self, n, logs):
    # def exclusiveTime(self, n, logs):
        return
        #TODO: your code goes here

    # def exclusiveTime_PASSED(self, n, logs):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        retlst = [0 for x in range(n)]
        s = logs[0].split(':')
        stk = [ord(s[0]) - 48]
        prev = ord(s[2]) - 48
        i = 1

        while i < len(logs):
            s = logs[i].split(':')
            s[0] = int(s[0])
            s[2] = int(s[2])
            if s[1] == 'start':
                if stk:
                    retlst[stk[-1]] += s[2] - prev
                stk.append(s[0])
                prev = s[2]
            else:
                retlst[stk[-1]] += (s[2] - prev) + 1
                prev = s[2] + 1
                stk.pop()

            i += 1

        return retlst


def main():
    Output: [3, 4]
    print(Solution().exclusiveTime(2, ["0:start:0",
                                       "1:start:2",
                                       "1:end:5",
                                       "0:end:6"]))

    # Output:
    print(Solution().exclusiveTime(3, ["0:start:0",
                                       "1:start:2",
                                       "1:end:5",
                                       "2:start:6",
                                       "2:end:8",
                                       "0:end:9"]))

    # Output: [5, 4, 4] ?
    print(Solution().exclusiveTime(3, ["0:start:0",
                                       "1:start:2",
                                       "1:end:5",
                                       "2:start:6",
                                       "2:end:9",
                                       "0:end:12"]))


# LC input
# 2
# ["0:start:0","1:start:2","1:end:5","0:end:6"]
# 3
# ["0:start:0","1:start:2","1:end:5","2:start:6","2:end:8","0:end:9"]
# 3
# ["0:start:0","1:start:2","1:end:5","2:start:6","2:end:9","0:end:12"]


if __name__ == '__main__':
    main()