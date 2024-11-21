import heapq

class Solution:
    def minOperations(self, v, k):
        q = []
        for num in v:
            heapq.heappush(q, num)
        c = 0
        while len(q) >= 2:
            if q[0] >= k:
                return c
            a = heapq.heappop(q)
            b = heapq.heappop(q)
            x = min(a, b) * 2 + max(a, b)
            heapq.heappush(q, x)
            c += 1
        return c
