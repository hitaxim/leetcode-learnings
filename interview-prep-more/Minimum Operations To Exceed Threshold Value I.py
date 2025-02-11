"""
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = 0
        for n in nums:
            if n < k:
                res += 1
        
        return res

"""
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        for i in range(0,len(nums)):
            if nums[i] < k:
                count += 1
            else:
                break
        return count
