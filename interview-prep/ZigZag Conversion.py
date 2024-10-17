class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == len(s) or numRows == 1: 
            return s
        
        rows = ['' for _ in range(numRows)]
        rowno = 0
        dirc = -1
        for i in range(len(s)):
            if rowno == (numRows - 1) or rowno == 0: 
                dirc *= -1
            rows[rowno] += s[i]
            rowno += dirc
        return ''.join(rows)
