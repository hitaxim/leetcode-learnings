class Solution:
   def largestAltitude(self, gain: List[int]) -> int:
       len_g = len(gain)
       c_alt = 0
       current_alt = []
       for i in range(len_g):
           current_alt.append(c_alt + gain[i])
           c_alt = c_alt + gain[i]
       ans = max(current_alt)
       if ans > 0:
           return ans
       else:
           return 0
