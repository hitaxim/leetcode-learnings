class Solution:
    def minLength(self, s: str) -> int:
        if not s: 
            return 0
        ans = []
        for char in s: 
            if not ans: 
                ans.append(char)
                continue
            if char == "B" and ans[-1] == "A":
                ans.pop()
            elif char == "D" and ans[-1] == "C":
                ans.pop()
            else: 
                ans.append(char)
        return len(ans)


class Solution:
    def minLength(self, s: str) -> int:
        while('AB' in s or 'CD' in s):
            if 'AB' in s:
                s = s.replace('AB','')
            
            if 'CD' in s:
                s = s.replace('CD','')
        
        return len(s)
        
