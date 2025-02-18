class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        if len(nums) <= 2:
            return nums[len(nums)-1]
        return nums[len(nums)-3]
