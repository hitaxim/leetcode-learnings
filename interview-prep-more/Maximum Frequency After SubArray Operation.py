class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        mxx = 0
        kc = nums.count(k)
        for i in range(1,51):
            if i == k: continue
            mx = 0
            c = 0
            for num in nums:
                if num == i: c += 1
                elif num == k: c -= 1
                mx = max(mx, c)
                c = max(0, c)
            mxx = max(mxx, mx)
        return kc + mxx
