class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return sorted(num & 1 for num in nums)
        
