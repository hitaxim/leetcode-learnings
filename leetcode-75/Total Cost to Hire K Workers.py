class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap_l = []
        heap_r = []
        totalCost = 0
        i = 0
        j = len(costs) - 1

        while k > 0: 
            while len(heap_l) < candidates and i <= j: 
                heapq.heappush(heap_l, costs[i])
                i += 1
            while len(heap_r) < candidates and i <= j: 
                heapq.heappush(heap_r, costs[j])
                j -= 1

            t1 = heap_l[0] if heap_l else float('inf')
            t2 = heap_r[0] if heap_r else float('inf')

            if t1 <= t2: 
                totalCost += t1
                heapq.heappop(heap_l)
            else:
                totalCost += t2
                heapq.heappop(heap_r)

            k -= 1
        return totalCost
