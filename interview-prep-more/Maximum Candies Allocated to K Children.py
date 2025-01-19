class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left, right = 0, max(candies)
        
        def canAllocate(mid):
            count = 0
            for candy in candies:
                count += candy // mid
            return count >= k
        
        while left < right:
            mid = (left + right + 1) // 2
            if canAllocate(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
