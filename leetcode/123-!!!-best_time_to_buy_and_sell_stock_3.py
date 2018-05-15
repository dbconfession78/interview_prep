# Instructions
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

class Solution:
    # def maxProfit_MINE(self, prices):
    def maxProfit(self, prices):
        _len = len(prices)
        if _len < 2:
            return 0
        local_min = prices[0]
        global_min = prices[0]
        i = 1
        gains = []
        max_gain = 0
        local_gain_count = 0
        hi_price_idx = 0
        while i < _len:
            if prices[i] > prices[hi_price_idx]:
                hi_price_idx = i
            if prices[i] < prices[i-1]:
                if i == _len - 1:
                    gains.append(max_gain)
                if prices[i -1] != local_min:
                    gains.append(prices[i-1] - local_min)
                    local_gain_count += 1
                    max_gain = max(max_gain, prices[i - 1] - global_min)
                local_min = prices[i]
            if prices[i] < global_min and i != _len-1:
                global_min = prices[i]
                gains.append(max_gain)
            i += 1

        if prices[i-1] > local_min:
            gains.append(prices[i-1] - local_min)
            local_gain_count += 1
            max_gain = max(max_gain, prices[i-1] - global_min)
            if hi_price_idx < i:
                gains.append(max_gain)
        if local_gain_count > 1:
            return gains[-1] + gains[-2]
        return max_gain

    def maxProfit_SPENCER(self, prices):
    # def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length < 2:
            return 0
        gains = []
        global_min = prices[0]
        local_min = prices[0]
        max_gain = prices[1] - prices[0]
        drop_count = 0

        i = 1
        while i < length:

            max_gain = max(max_gain, prices[i] - global_min)
            if prices[i] < prices[i-1]:
                drop_count += 1
                current_gain = prices[i-1] - local_min
                if gains:
                    x_gain = prices[i-1] - global_min
                    gains.append(x_gain)
                local_min = prices[i]
                if current_gain > 0:
                    gains.append(current_gain)
            if i == length - 1 and prices[i] > prices[i - 1]:
                gains.append(prices[i])


            global_min = min(global_min, prices[i])
            i += 1

        gains.sort()
        if len(gains) == 2:
            return sum(gains)
        if gains == [] and max_gain <= 0:
            return 0
        if len(gains) == 1:
            return gains[0]
        if drop_count > 1:
            return gains[-2] + gains[-3]
        if max_gain <= 0:
            return 0
        return max_gain

def main():
    print(Solution().maxProfit([]))                         # 0
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))         # 7
    print(Solution().maxProfit([7, 6, 4, 3, 1]))            # 0
    print(Solution().maxProfit([2, 17, 6, 4, 3, 11, 9]))    # 23
    print(Solution().maxProfit([40, 47, 46, 45, 19, 12, 14, 26, 30, 36, 57, 100, 80, 79, 110]))  # 119
    # print()
    print(Solution().maxProfit([1,2,4,2,5,7,2,4,9,0]))      # 13
    print(Solution().maxProfit([1]))                        # 0
    print(Solution().maxProfit([1, 2]))                     # 1
    print(Solution().maxProfit([4, 2, 1]))                  # 0
    print(Solution().maxProfit([2,1,2,0,1]))                # 2
    print(Solution().maxProfit([3,2,6,5,0,3]))              # 7
    print(Solution().maxProfit([1,2,4,2,5,7,2,4,9,0,9]))    # 17
    print(Solution().maxProfit([1,3,5,4,3,7,6,9,2,4]))    # 10 <--

# LC input
# []
# [7, 1, 5, 3, 6, 4]
# [7, 6, 4, 3, 1]
# [2, 17, 6, 4, 3, 11, 9]
# [40, 47, 46, 45, 19, 12, 14, 26, 30, 36, 57, 100, 80, 79, 110]
# [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
# [1]
# [1, 2]
# [4,2,1]
# [2,1,2,0,1]
# [3,2,6,5,0,3]
# [1,2,4,2,5,7,2,4,9,0,9]
# [1,3,5,4,3,7,6,9,2,4]




if __name__ == '__main__':
    main()

# LC input
# []
# [7, 1, 5, 3, 6, 4]
# [7, 6, 4, 3, 1]
# [2, 17, 6, 4, 3,11,9]
# [40, 47, 46, 45, 19, 12, 14, 26, 30, 36, 57, 100, 80, 79, 110]