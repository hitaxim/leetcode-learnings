class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cnt = 1
        max_cnt = 0
        if len(nums) == 1:
            return 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i -1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > max_cnt:
                max_cnt = cnt
            
        return max_cnt
