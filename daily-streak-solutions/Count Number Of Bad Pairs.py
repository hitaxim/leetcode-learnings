class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = {}
        good_pairs = 0

        for i, num in enumerate(nums):
            key = num - i
            good_pairs += freq.get(key, 0)
            freq[key] = freq.get(key, 0) + 1

        n = len(nums)
        return (n * (n - 1)) // 2 - good_pairs

"""
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        c=Counter(i-n for i,n in enumerate(nums))
        res=len(nums)*(len(nums)-1)
        
        for v in c.values():
            if v>1:
                res-=v*(v-1)
        return res//2
"""
