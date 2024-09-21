class Solution:
   def chalkReplacer(self, chalk: List[int], k: int) -> int:
       total_chalk = sum(chalk)
       rem = k % total_chalk
       for i, val in enumerate(chalk):
           rem -= val
           if rem < 0:
               return i
       return -1
