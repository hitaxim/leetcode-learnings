Class Solution:    
def longestOnes(self, nums: List[int], k: int) -> int:
       zero, start, end = 0, 0, 0
       while end < len(nums):
           if nums[end] == 0:
               zero += 1
           end += 1
           if zero > k:
               if nums[start] == 0:
                   zero -= 1
               start += 1
       return end - start
