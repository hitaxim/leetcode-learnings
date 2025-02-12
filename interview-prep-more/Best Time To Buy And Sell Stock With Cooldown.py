class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
		# initialization
        cool_down, sell, hold = 0, 0, -float('inf')
        
        for stock_price_of_Day_i in prices:
            
            prev_cool_down, prev_sell, prev_hold = cool_down, sell, hold
            
            # Max profit of cooldown on Day i comes from either cool down of Day_i-1, or sell out of Day_i-1 and today Day_i is cooling day
            cool_down = max(prev_cool_down, prev_sell)
            
            # Max profit of sell on Day_i comes from hold of Day_i-1 and sell on Day_i
            sell = prev_hold + stock_price_of_Day_i
            
            # Max profit of hold on Day_i comes from either hold of Day_i-1, or cool down on Day_i-1 and buy on Day_i
            hold = max(prev_hold, prev_cool_down - stock_price_of_Day_i)
        
        
        # The action of final trading day must be either sell or cool down
        return max(sell, cool_down)

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n==1: return 0

        dp=[[0]*5 for _ in range(2)]
        dp[0][0]=-prices[0]
        dp[0][1]=-prices[0]
        '''
        set hold balance the same as buy at time 0 is a tricky one
        if we set hold to 0, then hold=nothing=0, the buy/sell action may never be made since the first buy will set balance below 0, smaller than nothing
        some optimization could be made, like combining hold/sell together
        '''
        # for loop starts at time 1
        for i in range(1,n):
            dp[-1][0]=max(dp[0][3],dp[0][4])-prices[i] #buy
            dp[-1][1]=max(dp[0][0],dp[0][1])           #hold
            dp[-1][2]=max(dp[0][0],dp[0][1])+prices[i] #sell
            dp[-1][3]=dp[0][2]                         #cool
            dp[-1][4]=max(dp[0][3],dp[0][4])           #nothing
            # current state i will be previous state at i+1
            dp[0]=dp[-1]
            # initialize i+1
            dp[-1]=[0]*5
        return max(dp[0])

"""
