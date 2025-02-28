class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:


        b = sorted(boxTypes, key = lambda x:x[1], reverse=True )
        c = 0

        for box, n in b:
            if truckSize ==0:
                return c

            boxes = min(box, truckSize)
            c += boxes * n

            truckSize -= boxes
        return c

            
        
