class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n  for _ in range(4)]
        for num in nums:
            dp[num] -= 1
            dp[2] = min(dp[2], dp[1])
            dp[3] = min(dp[3], dp[2])

        return dp[3]
        
