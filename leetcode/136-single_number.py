class Solution:
    # def singleNumber_LC(self, nums):
    def singleNumber(self, nums):
        return sum(set(nums))*2 - sum(nums)


    def singleNumber_MINE(self, nums):
    # def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for elem in nums:
            d[elem] = d[elem] + 1 if d.get(elem) else 1

        return [k for k,v in d.items() if v == 1][0]



def main():
    print(Solution().singleNumber([1]))
    print(Solution().singleNumber([1, 5, 5, 2, 7, 3, 2, 1, 3]))


if __name__ == '__main__':
    main()

# Instructions
"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""