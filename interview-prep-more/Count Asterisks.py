class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        flag = True
        for ch in s:
            if flag and ch == "*":
                ans += 1
            if ch == "|":
                flag = not flag
        return ans
        
