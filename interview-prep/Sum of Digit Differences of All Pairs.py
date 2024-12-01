class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        d = len(str(nums[0]))
        c = len(nums)
        ds = 0
        for idx in range(d):
            nCount = {}
            for i in nums:
                s = str(i)
                n = s[idx]
                nCount[n] = nCount.get(n, 0) + 1
            
            nDifferences = 0
            nReduce = c
            for k, v in nCount.items():
                nReduce -= v
                nDifferences += (nReduce * v)
            
            ds += nDifferences
        
        return ds

        

"""
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        l = len(str(nums[0]))
        dp = [Counter() for _ in range(l)]
        ans = 0

        for i in range(len(nums)):
            for index, digit in enumerate(str(nums[i])):
                if digit in dp[index]:
                    ans -= dp[index][digit]
                ans += i
                dp[index] += Counter([digit])
        return ans
"""
