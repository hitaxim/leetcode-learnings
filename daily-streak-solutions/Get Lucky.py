class Solution:
   def getLucky(self, s: str, k: int) -> int:
       convert_n = ""
       for x in s:
           convert_n += str(ord(x)- 96)
     
       while k>0:
           temp = 0
           for x in convert_n:
               temp += int(x)
           convert_n = str(temp)
           k -= 1
       return int(convert_n)
