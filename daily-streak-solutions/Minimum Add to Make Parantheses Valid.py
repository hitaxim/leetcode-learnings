class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s: 
            return 0
        stack = []
        for c in s: 
            if c == ")":
                if stack: 
                    if stack[-1] == "(":
                        stack.pop()
                        continue
            
            stack.append(c)
        return len(stack)  
