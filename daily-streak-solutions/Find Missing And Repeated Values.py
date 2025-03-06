class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
       
        missing = (n * n) * (1 + n * n) // 2 
        seen = set() 
        duplicate = -1
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num not in seen:
                    seen.add(num)
                    missing -= num 
                else:
                    duplicate = num
                    
        return [duplicate, missing]
