class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        return max(self.helper(red, blue), self.helper(blue, red))
    
    def helper(self, red: int, blue: int) -> int:
        h = 0
        i = 1
        
        while True:
            if i % 2 == 1:
                if red >= i:
                    red -= i
                else:
                    break
            else:
                if blue >= i:
                    blue -= i
                else:
                    break
            h += 1
            i += 1
        
        return h
