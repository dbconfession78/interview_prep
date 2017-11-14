#!/usr/bin/python3

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        string = str(abs(x))
        length = len(string)

        i = 0
        j = length-1
        while (i < length):            
            if (string[i] != string[j]):
                return False
            i += 1
            j -= 1

        return True

            

sol = Solution()
num = sol.isPalindrome(-2147447412)
print('num: {}'.format(num))
