class Solution:
   def canConstruct(self, ransomNote: str, magazine: str) -> bool:
       ch_dict = {}
       for ch in magazine:
           ch_dict[ch] = ch_dict.get(ch, 0)+ 1
       for ch in ransomNote:
           if ch not in ch_dict or ch_dict[ch] <= 0:
               return False
           ch_dict[ch] -= 1
       return True
