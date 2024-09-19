class Solution:
   def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
       len_flower = len(flowerbed)
       if n == 0:
           return True
      
       for i in range(len_flower):
           if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len_flower - 1 or flowerbed[i+1] == 0):
               flowerbed[i] = 1
               n -= 1
               if n == 0:
                   return True
       return False
