class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = mx = mn = 0
        for x in nums: 
            mx = max(mx + x, 0)
            mn = min(mn + x, 0)
            ans = max(ans, mx, -mn)
        return ans 

"""
class Solution:
    def maxAbsoluteSum(self, nums):
        min_prefix_sum = 0
        max_prefix_sum = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            max_prefix_sum = max(max_prefix_sum, prefix_sum)

        return max_prefix_sum - min_prefix_sum
"""
