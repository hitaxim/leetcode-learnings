class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        counter = Counter(ranks)
        def canbedone(time):
            torepair = cars
            for rank, freq in counter.items():
                torepair -= math.floor((time/rank)**0.5) * freq
                if torepair <= 0:
                    return True

            return False

        left = min(ranks)
        right = max(ranks) * (cars**2)

        while left <= right:
            mid = left + (right - left) // 2
            if canbedone(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left 


            
