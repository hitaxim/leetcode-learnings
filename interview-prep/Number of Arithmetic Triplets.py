#### UNORDERED SET
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter = 0
        numSet = set(nums) 
        for num in nums:
            if (num + diff) in numSet and (num + 2 * diff) in numSet:
                counter += 1
        
        return counter    

"""
HASHMAP : 
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter = 0
        numSet = set(nums) 
        for num in nums:
            if (num + diff) in numSet and (num + 2 * diff) in numSet:
                counter += 1
        
        return counter

ARRAY : 
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter = 0
        for i in range(len(nums)):
            if self.contains(nums, nums[i] + diff) and self.contains(nums, nums[i] + 2 * diff):
                counter += 1
        return counter

    def contains(self, nums: List[int], target: int) -> bool:
        return target in nums

BRUTE FORCE: 
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[k] - nums[j] == diff and nums[j] - nums[i] == diff:
                        counter += 1
        return counter
"""
