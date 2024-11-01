class Solution:
    def makeFancyString(self, s: str) -> str:
        # Initialize an empty list to build the result string
        result = []
        
        for char in s:
            # Only add char if it does not form three consecutive same characters
            if len(result) < 2 or not (result[-1] == result[-2] == char):
                result.append(char)
        
        # Join the list into a string and return
        return ''.join(result)

"""
class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[0]
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == ans[-1]:
                cnt += 1
                if cnt < 3:
                    ans += s[i]
            else:
                cnt = 1
                ans += s[i]
        return ans       

"""
