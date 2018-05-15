from itertools import combinations
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        nums.sort()
        retlist = []

        for i in range(len(nums) - 2):
            j = len(nums) - 1
            while j > 0:
                if i > 0 and nums[i] == nums[i - 1]:
                    j -= 1
                    continue
                L = i + 1
                R = j - 1
                while L < R:
                    sum = nums[i] + nums[L] + nums[R] + nums[j]
                    if sum < target:
                        L += 1
                    elif sum > target:
                        R -= 1
                    else:
                        retlist.append([nums[i]
nums[L]
nums[R]
nums[j]])
                        while L < R and nums[L] == nums[L+1]:
                            L += 1
                        while R > L and nums[R] == nums[R-1]:
                            R -= 1
                        while j > 0 and nums[j] == nums[j-1]:
                            j -= 1
                        L += 1; R -= 1
                j -= 1

        return retlist


nums = [1, 0, -1, 0, -2, 2]
target = 0
nums = [5, 5, 3, 5, 1, -5, 1, -2]
target = 4


# inpt = input().strip('[]')
# if len(inpt) != 0:
#     nums = [int(x) for x in inpt.split(',')]


print(Solution().fourSum(nums, target))