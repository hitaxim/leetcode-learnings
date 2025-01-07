"""
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [nums[0]] + [0] * (len(nums) - 1 )
        for i in range(1, len(nums)):
            dp[i] = nums[i] + max(dp[max(0, i-k) : i])
        return dp[-1]


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        heap = [(0, -k)]
        for i in range(len(nums)):
            while i - heap[0][1] > k: 
                heappop(heap)
            nums[i] -= heap[0][0]
            heappush(heap, (-nums[i], i))
        
        return nums[-1]
"""

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        d = collections.deque([0])

        for i in range(1,n):
            while d and d[0] < i - k:
                d.popleft()

            dp[i] = dp[d[0]] + nums[i]

            while d and dp[d[-1]] <= dp[i]:
                d.pop()
            d.append(i)
        return dp[-1]
