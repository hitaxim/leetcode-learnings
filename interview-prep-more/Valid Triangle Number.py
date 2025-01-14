class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        if n < 3:
            return 0 
        
        nums.sort()

        for i in range(2, n):
            left, right = 0, i - 1
            
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += (right - left)
                    right -= 1
                else:
                    left += 1

        return count
