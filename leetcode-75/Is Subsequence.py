class Solution:
   def isSubsequence(self, s: str, t: str) -> bool:
       first = 0
       second = 0
       len_s = len(s)
       len_t = len(t)
       while first < len_s and second < len_t:
           if s[first] == t[second]:
               first += 1
           second += 1
       return first == len_s
