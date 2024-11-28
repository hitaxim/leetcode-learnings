class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)- 2):
            l, r = i + 1, len(nums) - 1
            while l < r: 
                currSum = nums[i] + nums[l] + nums[r]

                if currSum == target : 
                    return target
                
                if abs(currSum - target) < abs(close - target):
                    close = currSum 
                
                if target > currSum : 
                    l += 1
                else: 
                    r -= 1
        return close
