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
