class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        lists = [-x for x in gifts]
        heapq.heapify(lists)
        for i in range(k):
            x = -heapq.heappop(lists)
            heapq.heappush(lists, -int(math.sqrt(x)))
        return abs(sum(lists))


"""
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            x=max(gifts)
            gifts.remove(x)
            gifts.append(int(sqrt(x)))
        return sum(gifts)


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        i = 0
        while i < k: 
            gifts = sorted(gifts)
            sqrt = math.floor(math.sqrt(gifts[-1]))
            gifts[-1] = sqrt
            i += 1
        return sum(gifts)
"""
        
