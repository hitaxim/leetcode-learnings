class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        ans_arrow = 1
        points.sort(key=lambda x: x[1])

        end = points[0][1]
        for p in points: 
            start, end_balloon = p
            if start > end: 
                ans_arrow += 1
                end = end_balloon
                
        return ans_arrow
