class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def isPossible(maxSum):
            curr = count = 0
            for i in nums:
                count += (i + curr > maxSum)
                curr = curr + i if i + curr <= maxSum else i
            return count + 1 <= m
        
        lo, hi = max(nums), sum(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            if isPossible(mid): hi = mid - 1
            else: lo = mid + 1
        return lo
