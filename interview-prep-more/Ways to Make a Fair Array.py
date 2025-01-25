class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        ops = 0
        even, odd = sum(nums[0::2]), sum(nums[1::2])
    
        for i, num in enumerate(nums):
            # remove current number from even or odd
            if i % 2 == 0: even -= num
            else: odd -= num

            # check if even and odd are equal
            if even  == odd : ops += 1
            
            # add to the opposite
            if i % 2 == 0: odd += num
            else: even += num
        
        return ops
