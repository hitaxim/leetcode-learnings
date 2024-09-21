class Solution:
   def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
       count = 0
       len_r = len(rolls)
       total_sum = (len_r + n) * mean
       rem_sum = total_sum - sum(rolls)
      
       if rem_sum < n or rem_sum > 6* n:
           return []
      
       base = rem_sum // n
       rem = rem_sum % n

       result = [base] * n
       for i in range(rem):
           result[i] += 1
      
       return result
