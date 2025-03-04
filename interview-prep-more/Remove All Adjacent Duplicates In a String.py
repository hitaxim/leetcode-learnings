class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        for ch in s:
            if stk and stk[-1] == ch:
                stk.pop()
            else:
                stk.append(ch)
        
        return "".join(stk)
        
