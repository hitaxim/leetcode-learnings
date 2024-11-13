class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        cnt = 0
        for i in range(len(nums) - 1, -1, -1):
            x = nums[i]
            lo = bisect_left(nums, lower - x, 0, i)
            hi = bisect_right(nums, upper - x, 0, i)
            cnt += hi - lo
        return cnt
