class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        res = []
        if len(nums) <= 1:
            return 0
        nums = sorted(nums)
        for i in range(len(nums)-1):
            res.append(nums[i+1]-nums[i])
        return max(res)
