"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            v = nums[m]
            if nums[m] == target:
                return m

            left_lst = nums[0:m]
            right_lst = nums[m+1:r+1]
            if not left_lst and not right_lst:
                return -1
            if left_lst and left_lst[0] < left_lst[-1] and v > left_lst[-1]:
                if target >= left_lst[0] and target <= left_lst[-1]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if right_lst and target >= right_lst[0] and target <= right_lst[-1]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


        # while l <= r:
        #     m = l + (r - l) // 2
        #     v = nums[m]
        #     if target == v:
        #         return m
        print()
        #     if nums[l] <= v:
        #         if nums[l] <= target and target <= v:
        #             r = m - 1
        #         else:
        #             l = m + 1
        print()
        #     else:
        #         if nums[m] <= target and target <= nums[r]:
        #             l = m + 1
        #         else:
        #             r = m - 1
        #
        # return -1

def main():
    print(Solution().search([], 5))                     # -1
    print(Solution().search([6,7,8,9,1,2,3,4,5], 6))    # 0
    print(Solution().search([5,6,7,8,9,1,2,3,4], 6))    # 1
    print(Solution().search([4,5,6,7,8,1,2,3], 8))      # 4
    print(Solution().search([5,1,3], 3))                # 2
    print(Solution().search([1], 2))                    # -1
    print(Solution().search([3,1], 2))                  # -1
    print(Solution().search([3,1], 1))                  # 1
    print(Solution().search([1,3], 0))                  # -1
    print(Solution().search([2,3,4,5,6,7,8,9,1], 9))    # 7
    print(Solution().search([1,3,5], 0))                # -1
    print(Solution().search([4,5,6,7,0,1,2], 3))        # -1

# LC Input
# []
# 5
# [6,7,8,9,1,2,3,4,5]
# 6
# [5, 6,7,8,9,1,2,3,4]
# 6
# [4,5,6,7,8,1,2,3]
# 8
# [1]
# 2
# [5,1,3]
# 3
# [1]
# 2
# [3,1]
# 2
# [3,1]
# 1
# [1,3]
# 0
# [2,3,4,5,6,7,8,9,1]
# 9
# [1,3,5]
# 0
# [4,5,6,7,0,1,2]
# 3

if __name__ == '__main__':
    main()