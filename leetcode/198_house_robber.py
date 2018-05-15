# Instructions
"""

"""


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _len = len(nums)
        money1 = 0
        money2 = 0
        money3 = 0
        i = 0
        l = 0
        r = _len - 1
        mid_i = _len // 2
        while i < _len:
            if i % 2 == 0:
                money1 += nums[i]
            else:
                money2 += nums[i]

            if l < r:
                if r == mid_i:
                    money3 += max(nums[l], nums[r])
                else:
                    money3 += nums[l] + nums[r]
                l += 2
                r -= 2
            i += 1
        if _len % 2 != 0:
            return max(money1, money2, money3)
        return max(money1, money2)






def main():
    # print(Solution().rob([]))                       # 0
    # print(Solution().rob([1,2,3,4,5,6,7,8,9,10]))   # 30
    # print(Solution().rob([1]))                      # 1
    # print(Solution().rob([20,30]))                  # 30
    # print(Solution().rob([2,1,1,2]))                # 4
    # print(Solution().rob([2,1,1,2,1,2]))            # 6
    # print(Solution().rob([30,1,1,2,1,40]))          # 72
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
