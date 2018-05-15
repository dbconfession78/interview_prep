# Instructions
"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""

from collections import Counter
class Solution:
    # def intersect_PRACTICE(self, nums1, nums2):
    def intersect(self, nums1, nums2):
        return



    def intersect_MINE2(self, nums1, nums2):
    # def intersect(self, nums1, nums2):
        if len(nums1) < len(nums2):
            short = nums1
            long = nums2
        else:
            short = nums2
            long = nums1

        count_short = Counter()
        count_long = Counter()
        retlist = []
        for elem in short:
            count_short[elem] += 1
        for elem in long:
            count_long[elem] += 1

        for k, v in count_long.items():
            x = count_short.get(k)

            if x:
                retlist += [k] * min(x, v)
        return retlist


def main():
    print(Solution().intersect([],[]))                         # []
    print(Solution().intersect([1, 2, 2, 1],[2, 2]))           # [2, 2]
    print(Solution().intersect([1, 7, 3, 5, 2],[8, 3, 7, 9]))  # [3, 7]
    print(Solution().intersect([1, 2, 3, 4],[5, 1, 2, 3, 4]))  # [1,2,3,4]
    print(Solution().intersect([3, 1, 2],[1, 3]))              # [1,3]
    print(Solution().intersect([4, 9, 5],[9, 4, 9, 8, 4]))     # [4,9]
    print(Solution().intersect([1, 2],[1, 1]))                 # [1]
    print(Solution().intersect([1],[1]))                       # [1]
    print(Solution().intersect([1],[1,1]))                     # [1]
    print(Solution().intersect([2,1],[1,1]))                   # [1]
    print(Solution().intersect([2,1],[1,2]))                   # [1,2]
    print(Solution().intersect([1,2,2,1],[1,2]))               # [1,2]
    print(Solution().intersect([1,2,2,1],[1,1]))               # [1,1]

# LC input
# []
# []
# [1, 2, 2, 1]
# [2, 2]
# [1, 7, 3, 5, 2]
# [8, 3, 7, 9]
# [1,2,3,4]
# [5,1,2,3,4]
# [3,1,2]
# [1,3]
# [4,9,5]
# [9,4,9,8,4]
# [1,2]
# [1,1]
# [1]
# [1]
# [1]
# [1,1]
# [2,1]
# [1,1]
# [2,1]
# [1,2]
# [1,2,2,1]
# [1,2]
# [1,2,2,1]
# [1,1]

if __name__ == '__main__':
    main()