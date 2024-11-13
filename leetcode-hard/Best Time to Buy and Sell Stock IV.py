class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if n == 0 or k == 0:
            return 0
        
        buyPrice = [float('inf')] * k
        profit = [float('-inf')] * k 

        for p in prices: 
            for i in range(k):
                buyPrice[i] = min(buyPrice[i], p - (profit[i-1] if i > 0 else 0))
                profit[i] = max(profit[i], p - buyPrice[i])
        
        return profit[k-1]
        
