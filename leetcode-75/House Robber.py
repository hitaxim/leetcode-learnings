class Solution:
   def rob(self, nums: List[int]) -> int:
       sum_1, sum_2 = 0, 0
       for x in nums:
           temp = max( x + sum_1, sum_2)
           sum_1 = sum_2
           sum_2 = temp
       return sum_2
