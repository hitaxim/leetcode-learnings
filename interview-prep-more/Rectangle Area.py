class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, 
                          bx1: int, by1: int, bx2: int, by2: int) -> int:

        overLapX1 = max(ax1, bx1)
        overLapX2 = min(ax2, bx2)
        downY1 = max(ay1, by1)
        upY2 = min(ay2, by2)

        overlapArea = 0
        if overLapX2 > overLapX1 and upY2 > downY1:
            overlapArea = (overLapX2 - overLapX1) * (upY2 - downY1)

        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        
        return area1 + area2 - overlapArea
