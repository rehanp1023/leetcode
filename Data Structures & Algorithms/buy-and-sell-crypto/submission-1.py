class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        days = len(prices)
        maxprofit = 0
        while sell < days:
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                if profit > maxprofit:
                    maxprofit = profit
                sell += 1
            else:
                buy = sell
                sell += 1
        return maxprofit
            