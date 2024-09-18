class Solution:
   def longestSubarray(self, nums: List[int]) -> int:
       maxBitwise = max(nums)
       maxi = 1
       count = 0
       i = 0


       while i < len(nums):
           if nums[i] == maxBitwise:
               while i < len(nums) and nums[i] == maxBitwise:
                   count += 1
                   i += 1
               maxi = max(maxi, count)
               count = 0
           else:
               i += 1
       return maxi
