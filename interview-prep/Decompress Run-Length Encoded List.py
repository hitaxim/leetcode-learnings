class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(0, n, 2):
            f = nums[i]
            val = nums[i+1]
            while f: 
                res.append(val)
                f -= 1
        return res
        
