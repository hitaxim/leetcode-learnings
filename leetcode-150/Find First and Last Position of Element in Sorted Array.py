class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(isLeft):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target or (isLeft and nums[mid] == target):
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        leftIndex = binarySearch(True)
        if leftIndex >= len(nums) or nums[leftIndex] != target:
            return [-1, -1]
        
        rightIndex = binarySearch(False) - 1
        return [leftIndex, rightIndex]
