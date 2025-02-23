class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        expected = heights.copy()
        expected.sort()

        c = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                c += 1
        return c
        
