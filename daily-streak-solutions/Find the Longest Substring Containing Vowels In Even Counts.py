class Solution:
   def findTheLongestSubstring(self, s: str) -> int:
       vowels = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16}
       first_occ = {0: -1}
       mask = 0
       max_len = 0


       for i, c in enumerate(s):
           if c in vowels:
               mask ^= vowels[c]
           if mask in first_occ:
               max_len = max(max_len, i-first_occ[mask])
           else:
               first_occ[mask] = i
       return max_len
