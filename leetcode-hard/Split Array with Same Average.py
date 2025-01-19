from typing import List

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        n = len(nums)
        
        # If there's only one element, we cannot split it into two non-empty subsets
        if n == 1:
            return False
        
        # Helper function to calculate the possible subset sums
        def possible_sums(arr: List[int]) -> int:
            subset_sums = 1
            for a in arr:
                subset_sums |= (subset_sums << a)
            return (subset_sums - 1) ^ (1 << sum(arr))
        
        # Transform nums to the differences from the target average
        transformed_nums = [n * num - total_sum for num in nums]
        
        # If there's a zero in transformed_nums, we can split directly
        if 0 in transformed_nums:
            return True
        
        # Split transformed numbers into positive and negative
        positives = [num for num in transformed_nums if num > 0]
        negatives = [-num for num in transformed_nums if num < 0]
        
        # Check if there's an overlap in achievable sums from positive and negative numbers
        return bool(possible_sums(positives) & possible_sums(negatives))

"""
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        total = sum(nums)

        @lru_cache()
        def dfs(i, sumA, lenA):
            if i == len(nums):
                if sumA * len(nums) == total * lenA and lenA > 0 and lenA != len(nums):
                    return True
                else:
                    return False
            
            res = dfs(i + 1, sumA + nums[i], lenA + 1) or dfs(i + 1, sumA, lenA)
            return res

        broke = False       
        for i in range(1, len(nums)):
            if total * i % len(nums) == 0:
                broke = True
                break
        if not broke:
            return False

        return dfs(0, 0, 0)
"""
