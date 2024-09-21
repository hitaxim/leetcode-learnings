class Solution:
   def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
       ans = 0
       for x in words:
           if set(x).issubset(set(allowed)):
               ans +=1
           #print(set(x), set(allowed))
       return ans
