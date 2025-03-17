class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for v in c.values():
            if v % 2 == 1:
                return False
        return True
        
