class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        ln = len(nums)
        dp = [False] * (ln + 1)
        dp[-1] = True
        for i in range(ln - 2, -1, -1):
            if nums[i] == nums[i + 1] and dp[i + 2]:
                dp[i] = True
            if i + 2 < ln:
                if nums[i] == nums[i + 1] and nums[i + 1] == nums[i + 2] and dp[i + 3]:
                    dp[i] = True
                if nums[i] == nums[i + 1] - 1 and nums[i + 1] == nums[i + 2] - 1 and dp[i + 3]:
                    dp[i] = True
        return dp[0]
