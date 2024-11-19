class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        x = nums.index(min(nums)) + 1
        y = nums.index(max(nums)) + 1

        res = min(max(n - x + 1, n - y + 1), max(x, y))
        if x > y: 
            x, y = y, x
        
        option = x + (n - y) + 1
        res = min(res, option)

        return res if n > 2 else n
