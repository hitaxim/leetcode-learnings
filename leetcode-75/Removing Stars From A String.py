class Solution:
   def removeStars(self, s: str) -> str:
       stack1 = []
       for i in s:
           if i != '*':
               stack1.append(i)
           else:
               stack1.pop()
      
       return ''.join(stack1)
