class Solution:
    def magicalString(self, n: int) -> int:
        arr = [1, 2, 2]
        i = 2

        while len(arr) < n:
            arr.extend([arr[-1]^3]* arr[i])
            i += 1

        return arr[:n].count(1) 
        
