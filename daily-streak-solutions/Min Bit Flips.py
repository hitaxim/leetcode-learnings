class Solution:
   def minBitFlips(self, start: int, goal: int) -> int:
       ans = 0
       xor_result = start ^ goal


       while xor_result > 0:
           ans += xor_result & 1
           xor_result >>=1
       return ans

################ ORRRRRRRR
class Solution:
   def minBitFlips(self, start: int, goal: int) -> int:
       ans = 0
       xor_result = start ^ goal

       return bin(xor_result).count('1')
