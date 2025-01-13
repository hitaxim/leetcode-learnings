class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse = True)
        sm = ht = maximumHeight[0]

        for tower in maximumHeight[1:]:
            ht = min(ht - 1, tower)
            if ht == 0:
                return -1
            sm += ht
        
        return sm
        
