class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces += [len(s), 0]
        return " ".join(s[spaces[i-1]:spaces[i]] for i in range(len(spaces)-1))

"""
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        i, j = 0, 0
        n, m = len(s), len(spaces)

        while j < m: 
            if i == spaces[j]:
                result.append(' ')
                j += 1
            result.append(s[i])
            i += 1
        
        while i < n: 
            result.append(s[i])
            i += 1
        
        return ''.join(result)
"""
