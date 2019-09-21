class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(len(prices)):
            for j in range(1, len(prices)):
                if(i < j):
                    profit = prices[j] - prices[i]
                    if(profit > max_profit):
                        max_profit = profit
        return max_profit
        