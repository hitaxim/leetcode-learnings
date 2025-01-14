class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        res = 0
        for house in houses:
            left = bisect.bisect_right(heaters, house) - 1
            right = bisect.bisect_left(heaters, house)

            # if house is to left of all heaters
            if left < 0:
                res = max(res, heaters[0] - house)
            elif right >= len(heaters):
                res = max(res, house - heaters[-1])
            else:
                res = max(res, min(house - heaters[left], heaters[right] - house))

        return res
        
"""
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        l = 0
        r = 1e9
        n = len(houses)
        m = len(heaters)
        houses.sort()
        heaters.sort()
        def checkHeat(mid: int):
            fst = 0
            snd = 0
            while fst < n and snd < m:
                while fst < n and \
                heaters[snd]+mid >= houses[fst] and heaters[snd]-mid <= houses[fst]:
                    fst+=1
                snd+=1
            return (fst >= n)

        while l < r:
            mid = int((l+r)//2)
            if not checkHeat(mid):
                l = mid + 1
            else:
                r = mid
        
        return l
"""
