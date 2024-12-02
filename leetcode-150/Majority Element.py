class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        n = len(nums)
        for x in nums: 
            seen[x] = seen.get(x,0) + 1
            if seen[x] > n // 2:
                return x      
