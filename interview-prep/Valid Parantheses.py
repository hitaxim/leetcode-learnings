class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        maps = {')':'(', '}':'{',']':'['}

        for char in s: 
            if char in maps.values(): 
                ans.append(char)
            elif char in maps.keys():
                if not ans or maps[char] != ans.pop():
                    return False
        return not ans
