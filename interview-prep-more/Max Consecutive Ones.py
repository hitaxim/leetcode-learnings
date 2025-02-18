class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = result = 0
        
        for num in nums:
            if num == 1:
                result += 1
                maxi = max(maxi, result)
            else:
                result = 0
        return maxi
