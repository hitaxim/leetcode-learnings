class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ans = {}
        for i, val in enumerate(nums):
            if val in ans and abs(i - ans[val]) <= k:
                return True
            else: 
                ans[val] = i
        return False     
