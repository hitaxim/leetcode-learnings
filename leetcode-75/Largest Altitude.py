class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_alt = 0
        max_alt = 0
        for x in gain:
            curr_alt += x
            max_alt = max(max_alt, curr_alt)
        return max_alt

"""
        n = len(gain)
        alt = [0] * (n+1)
        for i in range(1,n+1):
            alt[i] = alt[i-1] + gain[i-1]
        return max(alt)

"""


"""
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

"""
