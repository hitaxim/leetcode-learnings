class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxVal = float('-inf')
        index = 0
        for i,num in enumerate(nums):
            if num > maxVal:
                maxVal = num
                index = i

        return index      
