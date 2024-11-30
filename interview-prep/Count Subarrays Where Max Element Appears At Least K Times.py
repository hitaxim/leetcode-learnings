class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxVal = max(nums)
        count = left = res = 0

        for val in nums:
            if val == maxVal: 
                count += 1
            while count >= k:
                if nums[left] == maxVal:
                    count -= 1
                left += 1
            
            res += left
        return res
