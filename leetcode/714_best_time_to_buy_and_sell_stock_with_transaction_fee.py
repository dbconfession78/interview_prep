"""
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""


class Solution(object):
    def maxProfit_PRACTICE(self, prices, fee):
    # def maxProfit(self, prices, fee):
        return

    # def maxProfit_SOL(self, prices, fee):
    def maxProfit(self, prices, fee):
        cash, hold = 0, -prices[0]
        for i in range(1, prices(len)):
            cash = max(cash, hold + prices[i] - 1)
            hold = max(hold, cash - prices[i])
        return cash

    def maxProfit_MINE(self, prices, fee):
    # def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        buy_val = prices[0]
        stk = [(0, 0, prices[0])]
        retval = 0
        while stk:
            i, profit, buy_val = stk.pop()
            retval = max(retval, profit)
            while i < len(prices):
                curr = prices[i]
                if i < len(prices)-1:
                    if curr >= buy_val and prices[i+1] < curr:
                        net_gain = profit + (curr-buy_val-fee)
                        buy_val = prices[i+1]
                        stk.append((i+1, net_gain, prices[i+1]))
                else:
                    if curr > prices[i-1] and curr > buy_val:
                        net_gain = profit + (curr - buy_val - fee)
                        buy_val = curr
                        stk.append((i+1, net_gain, buy_val))
                i += 1
        return retval


def main():
    print(Solution().maxProfit([1,3,2,8,4,9], 2))           # 8
    print(Solution().maxProfit([1,3,7,5,10,3], 3))          # 6
    print(Solution().maxProfit([4,5,2,4,3,3,1,2,5,4], 1))   # 4

#LC Input
# [1,3,2,8,4,9]
# 2
# [1,3,7,5,10,3]
# 3
# [4,5,2,4,3,3,1,2,5,4]
# 1

if __name__ == '__main__':
    main()