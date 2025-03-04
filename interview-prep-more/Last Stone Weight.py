import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heappush(heap, -1 * i)
        while(len(heap) > 1):
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            curr = (-1*y)-(-1*x)
            if(curr != 0):
                heapq.heappush(heap,-1*curr)
        if(len(heap) == 0):
            return 0
        else:
            return -1*heap[0]
        
