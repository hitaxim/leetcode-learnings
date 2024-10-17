class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i-1] < ratings[i] and candies[i-1] >= candies[i]:
                candies[i] = candies[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i+1] < ratings[i] and candies[i+1] >= candies[i]:
                candies[i] = candies[i+1] + 1
        
        return sum(candies)

  ## Check for the neighbors to have more ratings and less candies -- add more candies
"""
Check for the neighbors to have more ratings and less number of candies 

for i in range(1,n):
(R) i > I-1 and (C) I-1 >= I 
I = (I-1) + 1

for I in range(n-2, -1,-1)
(R) I+1 < I and (C) I =< I+1
I = (I+1) + 1
"""
