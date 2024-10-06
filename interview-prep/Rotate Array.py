class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cp = nums[:]
        n = len(nums)
        for i in range(n):
            v = (i + k) % n
            nums[v] = cp[i]
