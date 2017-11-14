#!/usr/bin/python3
import sys

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if type(x) != int:
            return
        print(sys.maxsize)
        new_string = str(abs(x))[::-1]
        retval = int(new_string);
        if x < 0:
            return retval * -1
        return(retval)


sol = Solution()
num = sol.reverse(1534236469)
print('num: {}'.format(num))
