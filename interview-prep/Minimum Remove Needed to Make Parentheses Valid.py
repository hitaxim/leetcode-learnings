class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else: 
                    to_remove.add(i)
        
        while stack: 
            to_remove.add(stack.pop())

        ans = []
        for i, ch in enumerate(s):
            if i not in to_remove:
                ans.append(ch)

        return "".join(ans)
