import math

class Solution:
    def checkPrime(self, x):
        if x <= 1: 
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0: 
                return False
        return True

    def primeSubOperation(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            bound = nums[i] if i == 0 else nums[i] - nums[i-1]
            if bound <= 0:
                return False
            largestPrime = 0
            for j in range(bound - 1, 1 , -1):
                if self.checkPrime(j):
                    largestPrime = j
                    break
            nums[i] -= largestPrime
        return True
        
