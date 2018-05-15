"""
Given an integer array sorted in ascending order, write a function to search target in nums.  If target exists, then return its index, otherwise return -1. However, the array size is unknown to you. You may only access the array using an ArrayReader interface, where ArrayReader.get(k) returns the element of the array at index k (0-indexed).

You may assume all integers in the array are less than 10000, and if you access the array out of bounds, ArrayReader.get will return 2147483647.



Example 1:

Input: array = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: array = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Note:

You may assume that all elements in the array are unique.
The value of each element in the array will be in the range [-9999, 9999].
"""

class ArrayReader:
    def __init__(self, lst):
        self.lst = lst

    def get(self, k):
        if abs(k) >= len(self.lst):
            return None
        else:
            return self.lst[k]

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """

        l = -1000
        r = 999
        print(r - l)
        if reader.get(l) < 0:
            if target > 0:
                while reader.get(l) < 0:
                    l += 1
            else:
                while reader.get(r) > 0:
                    r -= 1
        else:
            r = target + 1



        # r = l + target + 1
        # while not reader.get(r):
        #     r -= 1

        while l <= r:
            m = (l+r) //2
            v = reader.get(m)
            if v == target:
                return m
            if target < v:
                r = m - 1
            elif target > v:
                l = m + 1
        return -1



def main():
    print(Solution().search(ArrayReader([-1,0,3,5,9,12]), 9))   # 4
    print(Solution().search(ArrayReader([-1,0,3,5,9,12]), 3))   # 2
    print(Solution().search(ArrayReader([-1,0,3,5,9,12]), -1))   # 0
    print(Solution().search(ArrayReader([-7,-6,-5,-4,-3,-2,-1,4]), 4))  # 7
    print(Solution().search(ArrayReader([-7,-6,-5,-2,-1,8,15,21]), 15))  # 6



if __name__ == '__main__':
    main()