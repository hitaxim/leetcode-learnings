class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        ans = inf
        m = len(nums1)
        for x in range(m):
            for y in range(x + 1, m):
                j = 0
                seen = None
                for i in range(m):
                    if i not in (x, y):
                        diff = nums2[j] - nums1[i]
                        if seen is None: seen = diff
                        elif seen != diff: break
                        j += 1
                else: ans = min(ans, seen)
        return ans
        
