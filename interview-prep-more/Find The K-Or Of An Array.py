class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        
        dp = [0]*31
        
        for num in nums:
            i = 0    
            while num > 0:
                if num & 1 == 1:
                    dp[i] += 1
                i += 1
                num = num >> 1

        ans = 0
        for i,count in enumerate(dp):
            if count >= k:
                ans += 2**i
                
        return ans
