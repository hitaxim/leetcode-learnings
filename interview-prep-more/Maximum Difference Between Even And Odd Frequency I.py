class Solution:
    def maxDifference(self, s: str) -> int:
        count_char = Counter(s)
        odd = []
        even = []
        
       
        for val in count_char.values():
            if val % 2 == 0:  
                even.append(val)
            else: 
                odd.append(val)
        
        if not odd or not even:
            return 0
        
        return max(odd) - min(even)

        
