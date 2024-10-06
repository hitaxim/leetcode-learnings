class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_prof = 0
        for p in prices:
            if p < min_price:
                min_price = p
            profit = p - min_price
            max_prof = max(max_prof, profit)
        return max_prof
