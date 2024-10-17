class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = 0 

        l_max = [0] * n
        l_max[0] = height[0]
        for i in range(1, n):
            l_max[i] = max(height[i], l_max[i-1])

        r_max = [0] * n
        r_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            r_max[i] = max(height[i], r_max[i+1])

        for i in range(1, n-1):
            water += min(r_max[i], l_max[i]) - height[i]

        return water

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        
        return water
"""
