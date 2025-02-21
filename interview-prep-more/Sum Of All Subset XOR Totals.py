class Solution:
    def subsetXORSum(self, nums):
        xor_sum = 0
        for num in nums:
            xor_sum |= num  # Use bitwise OR to combine all bits
        return xor_sum * (1 << (len(nums) - 1))
