#!/usr/bin/python3
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = sorted(nums1 + nums2)
        length = len(nums3)
        if length % 2 == 0:
            a = float((nums3[int((length/2)-1)]))
            b = float((nums3[int(length/2)]))
            return ((a+b) / 2)
        else:
            return float(nums3[int(length/2)])
        
nums1 = [1, 3]
nums2 = [2, 4]
sol = Solution().findMedianSortedArrays(nums1, nums2)
print(sol)
