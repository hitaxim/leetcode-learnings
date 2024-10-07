class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        summ = sum(nums)
        if summ < abs(target) or (summ + target) & 1 : 
            return 0
        
        def knapsack(target):
            dp = [1] + [0] * summ
            for num in nums:
                for j in range(summ, num-1, -1):
                    dp[j] += dp[j - num]
            return dp[target]
        
        return knapsack((summ + target) //2)


"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        l=defaultdict(int)
        l[0]+=1
        for num in nums:
            newl=defaultdict(int)
            for i in l:
                newl[i+num]+=l[i]
                newl[i-num]+=l[i]
            l=newl
        return l[target]
"""   
