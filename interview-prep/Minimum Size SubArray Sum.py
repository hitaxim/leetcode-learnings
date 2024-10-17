class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_l = float('inf')
        r = 0
        sumv = 0
        l = 0
        while r < len(nums):
            sumv += nums[r]
            while sumv >= target:
                min_l = min(min_l, r - l +1)
                sumv -= nums[l]
                l += 1
            r += 1

        return 0 if min_l == float('inf') else min_l
