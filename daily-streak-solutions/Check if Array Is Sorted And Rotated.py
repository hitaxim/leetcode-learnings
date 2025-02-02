class Solution:
    def check(self, nums):
        n = len(nums)
        count = 0
        if nums[0] < nums[-1]:
            count += 1
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                count += 1
            if count > 1:
                return False
        return True
