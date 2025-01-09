class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = [['$', 0]]

        for c in s:
            if stk[-1][0] == c:
                stk[-1][1] += 1
                if stk[-1][1] == k:
                    stk.pop()
            else:
                stk.append([c, 1])
        
        return ''.join(c * cnt for c, cnt in stk)
        
