class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        storage = []
        for i in nums:
            if i-1 not in nums:
                left = i
                gap = 1
                while left + gap in nums:  # find consecutive range
                    gap += 1
                if gap > 1:
                    storage.append(f"{i}->{left + gap - 1}")  
                else:
                    storage.append(str(i))  # only itself
        return storage

ORRRRRRRRR

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if not nums: 
            return ans
        start = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    ans.append(str(start))
                else:
                    ans.append(f"{start}->{nums[i-1]}")
                start = nums[i]
        if start == nums[-1]:
            ans.append(str(start))
        else: 
            ans.append(f"{start}->{nums[-1]}")
        return ans
