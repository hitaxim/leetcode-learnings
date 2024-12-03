class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums: 
            return nums.index(target)
        index = bisect_left(nums,target)
        return index
        
