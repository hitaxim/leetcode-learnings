class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        stack = []
        for i in range(len(pattern)+1): 
            stack.append(str(i+1))
            if i == len(pattern) or pattern[i] == 'I': 
                while stack: ans.append(stack.pop())
        return ''.join(ans) 

"""
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        pattern += 'I'
        res = s = ''
        for i,p in enumerate(pattern):
            s += str(i+1)
            if p == 'I':
                res += s[::-1]
                s =''
        return res
"""
