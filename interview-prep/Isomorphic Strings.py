class Solution:
   def isIsomorphic(self, s: str, t: str) -> bool:
       if len(s) != len(t):
           return False
       ans_s = []
       ans_t = []
       for j in s:
          ans_s.append(s.index(j))
       for c in t:
          ans_t.append(t.index(c))
       if ans_t == ans_s:
           return True
       return False
