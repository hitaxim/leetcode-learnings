class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        ans = sm = lg = mx = 0
        for x, y in zip(nums1, nums2):
            if mx < min(x, y):
                ans += min(sm, lg)
                sm = lg = 0
            mx = max(x, y)
            if x < y: sm += 1
            elif x > y : lg += 1
        return ans + min(sm, lg)
