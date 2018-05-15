# 278. First Bad Version
"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version
of your product fails the quality check. Since each version is developed based on the previous version, all the
versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the
following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to
find the first bad version. You should minimize the number of calls to the API.
"""
# *** when pasting into LC, remove 2nd param, bv (bad version) from method def and calls


class Solution:
    # def firstBadVersion_PRACTICE(self, n, bv):
    def firstBadVersion(self, n, bv):
        return

    def firstBadVersion_PASSED(self, n, bv):
    # def firstBadVersion(self, n, bv):
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid, bv):
                right = mid
            else:
                left = mid + 1
        return left


def isBadVersion(n, bad_version):
    if n >= bad_version:
        return True
    else:
        return False


def main():
    print(Solution().firstBadVersion(2, bv=1))
    print(Solution().firstBadVersion(3, bv=1))
    print(Solution().firstBadVersion(4, bv=4))
    print(Solution().firstBadVersion(2126753390, bv=1702766719))


# * When pasting into LC, remove 2nd param, bv (bad version) from method def and calls
if __name__ == '__main__':
    main()
