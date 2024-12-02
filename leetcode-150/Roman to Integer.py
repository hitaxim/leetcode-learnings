class Solution:
    def romanToInt(self, s: str) -> int:
        ans = {'I':1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        index = len(s)
        sum = 0
        for i in range(index):
            if i <index -1 and ans[s[i]] < ans[s[i+1]]:
                sum -= ans[s[i]]
            else: 
                sum += ans[s[i]]
        return sum

