class Solution:
   def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
       max_candy = max(candies)
       len_candy = len(candies)
       result = [False] * len_candy
       for i in range(len_candy):
           if candies[i] + extraCandies >= max_candy:
               result[i] = True
       return result
