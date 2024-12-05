class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        nums = arr
        while l<=r:
            mid = l+(r-l)//2
            
            if nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid+1]>nums[mid]:
                l=mid+1
            else:
                r = mid-1
                
"""
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(len(arr) - 1):
            if arr[i] < arr[i+1]:
                i += 1
            else:
                break
        return i
"""    
