class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def findLongestConsecELement(numSet):
            res = 1
            for num in numSet: 
                count = 1
                current = num

                while current + 1 in numSet:
                    current += 1
                    count += 1
                res = max(res, count)
            return res
        
        res = 1
        if len(hBars) == 0 or len(vBars) == 0: return 1

        hSet, vSet = set(hBars), set(vBars)
        maxHBars, maxVBars = findLongestConsecELement(hSet), findLongestConsecELement(vSet)

        return (min(maxHBars, maxVBars) + 1) ** 2
