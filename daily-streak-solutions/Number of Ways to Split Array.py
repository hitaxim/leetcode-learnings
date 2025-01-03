class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        lsum = 0
        rsum = sum(nums)
        ans = 0
        for i in range(len(nums) - 1):
            lsum += nums[i]
            rsum -= nums[i]
            if lsum >= rsum: 
                ans += 1
                
        return ans
