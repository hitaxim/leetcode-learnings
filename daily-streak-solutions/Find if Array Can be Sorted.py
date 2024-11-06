from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # Helper function to count set bits
        def setBits(num):
            count = 0
            for i in range(31, -1, -1):
                if ((num >> i) & 1) == 1:
                    count += 1
            return count

        # Helper function to check if array is sorted
        def check(nums):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True

        # Array to store the set bit count of each number
        count = [setBits(num) for num in nums]

        n = len(nums)
        k = 0
        while k < n:
            for i in range(1, n):
                if count[i] == count[i - 1] and nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]  # Swap elements
            if check(nums):
                return True
            k += 1

        return False

"""
class Solution:
    def haveSameSetBits(self, a: int, b: int) -> bool:
        # Python equivalent of __builtin_popcount(a) to count set bits
        return bin(a).count('1') == bin(b).count('1')
    
    def canSortArray(self, nums: list[int]) -> bool:
        N = len(nums)
        times = N
        
        # Perform bubble sort-like operation with condition on set bits
        for _ in range(times):
            for i in range(N - 1):
                if self.haveSameSetBits(nums[i], nums[i + 1]) and nums[i + 1] < nums[i]:
                    # Swap the elements
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        
        # Check if the array is sorted
        return nums == sorted(nums)   
"""   
