class Solution:        
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        minLens = {}
        secondMin = float('inf')
        
        for point, char in zip(points, s):
            size = max(abs(point[0]), abs(point[1]))

            if char not in minLens:
                minLens[char] = size
            elif size < minLens[char]:
                secondMin = min(minLens[char], secondMin)
                minLens[char] = size
            else:
                secondMin = min(size, secondMin)
        
        count = 0
        for len in minLens.values():
            if len < secondMin:
                count += 1
        
        return count
