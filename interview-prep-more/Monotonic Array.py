class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        
        # check if this is increasing        
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                break
            
            if i == n - 1:
                return True

        # check if this is decreasing
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                break
            
            if i == n - 1:
                return True

        return False

"""
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True

        is_inc = True
        is_dec = True

        for i in range(1, n):
            if not is_inc and not is_dec:
                return False

            if nums[i] < nums[i-1]:
                is_inc = False
            if nums[i] > nums[i-1]:
                is_dec = False

        return is_inc or is_dec
"""
