# Instructions
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        gain = 0
        i = 1
        _len = len(prices)
        while i < _len:
            if prices[i] > prices[i-1]:
                gain += prices[i] - prices[i-1]
            i += 1
        return gain



def main():
    print(Solution().maxProfit([]))                     # 0
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))     # 7
    print(Solution().maxProfit([7, 6, 4, 3, 1]))        # 0
    print(Solution().maxProfit([2, 17, 6, 4, 3, 11, 9]))  # 23
    print(Solution().maxProfit([40, 47, 46, 45, 19, 12, 14, 26, 30, 36, 57, 100, 80, 79, 110]))  # 126



# 1/9/18
# plan -> keys: 22 min
# keys -> debug (first submit): +11 min
# debug -> accepted: +12 min
# Total 45 min

if __name__ == '__main__':
    main()

# LC input
# []
# [7, 1, 5, 3, 6, 4]
# [7, 6, 4, 3, 1]
# [2, 17, 6, 4, 3,11,9]
# [40, 47, 46, 45, 19, 12, 14, 26, 30, 36, 57, 100, 80, 79, 110]