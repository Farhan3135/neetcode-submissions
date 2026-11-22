class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = 0
        sell = 0
        while sell<len(prices):
            if prices[buy]<= prices[sell]:
                maxProfit = max(maxProfit, prices[sell] - prices[buy])
                sell +=1
            else:
                buy = sell
        return maxProfit