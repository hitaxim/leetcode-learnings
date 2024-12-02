class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        cp = nums[:]
        for i in range(n):
            t = (i + k) % n
            nums[t] = cp[i]
        return nums
