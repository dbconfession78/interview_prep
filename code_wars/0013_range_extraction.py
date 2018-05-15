"""
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example ("12, 13, 15-17")
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
"""

class Solution():
    def solution(self, args):
        _len = len(args)
        i = 0
        range = []
        retval = ""
        while i < _len:
            _this = args[i]
            if i < _len-1:
                nxt = args[i+1]
            range.append(_this)
            if i < _len and _this != nxt-1:
                if len(range) > 1:
                    if len(range) == 2:
                        retval += "{},{}".format(str(range[0]), str(range[1]))
                    else:
                        retval += "{}-{}".format(str(range[0]), str(range[-1]))
                    if i != _len-1:
                        retval += ","
                    range = []
                else:
                    retval += str(range.pop())
                    if i != _len-1:
                        retval += ","
            i += 1
        return retval


def main():
    print(Solution().solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))      # "-6,-3-1,3-5,7-11,14,15,17-20"




if __name__ == '__main__':
    main()