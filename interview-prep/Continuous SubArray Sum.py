class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_cache = {0 : -1}
        rem = 0

        for i in range(len(nums)):
            rem += nums[i]
            rem %= k
            if rem not in rem_cache:
                rem_cache[rem] = i 
            elif i - rem_cache[rem] >= 2:
                return True
        return False
