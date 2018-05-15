# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool



class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        L = 0
        R = n
        M = R // 2
        while (R-L) > 1:
            if self.isBadVersion(M):
                R = M
                M = (R - L) // 2
            else:
                L = M
                M = (R - L) // 2 + L
        return R


    def isBadVersion(self, version):
        # if version >= 7:
        if version >= 1702766719:
        # if version >= 1:
            return True
        return False



def main():
    # print(Solution().firstBadVersion(100))
    # print(Solution().firstBadVersion(9))
    print(Solution().firstBadVersion(2126753390)) # bad is 1702766719
    # print(Solution().firstBadVersion(2))  # bad is 1


if __name__ == '__main__':
    main()

# Instructions
"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""