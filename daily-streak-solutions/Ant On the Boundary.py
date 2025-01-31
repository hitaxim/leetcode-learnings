class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        sum_val = 0
        count = 0
        for num in nums:
            sum_val += num
            if sum_val == 0:
                count += 1
        return count
        
