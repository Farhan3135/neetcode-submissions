class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = 0
        sell = 0
        maxProfit=0
        
        while sell != len(prices)-1:
            if prices[sell]<prices[buy]:
                buy = sell
            
            while sell != len(prices)-1 and prices[sell]>= prices[buy]:
                
                sell+=1
                maxProfit = max(maxProfit, prices[sell]-prices[buy])
            
        return maxProfit
                
            
