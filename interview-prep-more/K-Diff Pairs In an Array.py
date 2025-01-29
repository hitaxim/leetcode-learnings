class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        total = 0
        if k < 0:
            return 0
        
        counts = Counter(nums)
        for n in counts:
            if k == 0:
                if counts[n] > 1:
                    total += 1
            else:
                if n + k in counts:
                    total += 1
        return total
