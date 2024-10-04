class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        len_n = len(nums)
        if len_n < 3:
            return False

        num1 = float('inf')
        num2 = float('inf')
        for x in nums:
            if x <= num1: 
                num1 = x
            elif x <= num2:
                num2 = x
            else: 
                return True
        return False
