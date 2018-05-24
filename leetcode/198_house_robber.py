# Instructions
"""

"""


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_max = 0
        curr_max = 0
        _len = len(nums)
        for x in range(_len):
            tmp = curr_max
            curr_max = max(prev_max + nums[x], curr_max)
            prev_max = tmp
        return curr_max







def main():
    print(Solution().rob([]))                       # 0
    print(Solution().rob([1,2,3,4,5,6,7,8,9,10]))   # 30
    print(Solution().rob([1]))                      # 1
    print(Solution().rob([20,30]))                  # 30
    print(Solution().rob([2,1,1,2]))                # 4
    print(Solution().rob([2,1,1,2,1,2]))            # 6
    print(Solution().rob([30,1,1,2,1,40]))          # 72
    print(Solution().rob([1,3,1,3,100]))            # 103


# LC input
# []
# [1,2,3,4,5,6,7,8,9,10]
# [1]
# [20, 30]
# [2,1,1,2]
# [2,1,1,2,1,2]
# [30,1,1,2,1,40]
# [1,3,1,3,100]

if __name__ == '__main__':
    main()

"""
class Solution:
    def func(self):
        return

def main():
    print(Solution().func())


if __name__ == '__main__':
    main()

"""
