# Instructions:
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""
class Solution:
    # def findMedianSortedArrays_PRACTICE(self, nums1, nums2):
    def findMedianSortedArrays(self, nums1, nums2):
        return

    def findMedianSortedArrays_PASSED(self, nums1, nums2):
    # def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = self.merge(nums1, nums2)
        _len = len(nums3)
        mid = _len // 2
        if _len % 2 == 0:
            return (nums3[mid] + nums3[mid - 1]) / 2
        return float(nums3[mid])

    def merge(self, nums1, nums2):
        i = j = 0
        retlist = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                retlist.append(nums1[i])
                i += 1;
            else:
                retlist.append(nums2[j])
                j += 1
        while i < len(nums1):
            retlist.append(nums1[i])
            i += 1
        while j < len(nums2):
            retlist.append(nums2[j])
            j += 1
        return retlist


print(Solution().findMedianSortedArrays([1, 3], [2]))
print(Solution().findMedianSortedArrays([1, 2], [3, 4]))


# LC INPUT
# [1,3]
# [2]
# [1,2]
# [3,4]