class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            heapq.heappush(q, num)
        c = 0
        while len(q) >= 2: 
            if q[0] >= k:
                return c
            a = heapq.heappop(q)
            b = heapq.heappop(q)
            x = min(a, b) * 2 + max(a, b)
            heapq.heappush(q,x)
            c += 1
        return c


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ops = 0

        heapify(nums)

        while True:
            x = heappop(nums)

            if x >= k:
                return ops
            y = heappop(nums)

            heappush(nums, x*2 + y)
            ops += 1
