class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        operation = 0
        len_n = len(nums)
        l = 0
        r = len_n - 1
        while l < r: 
            if nums[l] + nums[r] == k:
                operation += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else: 
                r -= 1
        return operation
