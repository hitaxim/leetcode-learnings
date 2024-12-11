"""
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        events = []
        for n in nums:
            events.append((n - k, 1))
            events.append((n + k + 1, -1))
        
        events.sort()

        max_beauty = 0
        curr_count = 0

        for val, effect in events:
            curr_count += effect
            max_beauty = max(max_beauty, curr_count)
        
        return max_beauty
"""

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l, ans = 0, 0
        
        for i, num in enumerate(nums):
            while l < n and nums[l] < num - 2*k :
                l += 1
            
            ans = max(ans, i - l + 1)

        return ans
