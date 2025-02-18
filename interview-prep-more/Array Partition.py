class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        totalsum=0
        l = len(nums)
        for i in range(0,l,2):
            totalsum += nums[i]
        return totalsum
