class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = curr_sum = nums[0]

        for a, b in pairwise(nums):
            curr_sum = curr_sum + b if a < b else b
            ans = max(ans, curr_sum)
    
        return ans
        
