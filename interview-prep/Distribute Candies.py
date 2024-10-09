class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        can_eat = len(candyType) // 2
        n_c = len(set(candyType))
        if n_c == can_eat: 
            return n_c
        elif n_c < can_eat: 
            return n_c
        else: 
            return can_eat
