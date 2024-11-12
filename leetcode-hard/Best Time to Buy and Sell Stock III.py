class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        first_buy = float('-inf')
        first_sell = 0
        second_buy = float('-inf')
        second_sell = 0

        for price in prices:
            first_buy = max(first_buy,-price)
            first_sell = max(first_sell,first_buy+price)
            second_buy = max(second_buy, first_sell - price)
            second_sell = max(second_sell, second_buy + price)

        return second_sell
