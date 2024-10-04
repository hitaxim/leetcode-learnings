class Solution:
    def maxArea(self, height: List[int]) -> int:
        len_n = len(height)
        max_w = 0
        l = 0
        r = len_n - 1
        while l < r: 
            max_w = max(max_w, min(height[l],height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_w
