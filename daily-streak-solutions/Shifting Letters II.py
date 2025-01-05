class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        cum_shift = [0 for _ in range(len(s) + 1)]

        for st, end, d in shifts:
            if d == 0:
                cum_shift[st] -= 1
                cum_shift[end + 1] += 1
            else:
                cum_shift[st] += 1
                cum_shift[end +1 ] -= 1
        
        cum_sum = 0
        for i in range(len(s)):
            cum_sum += cum_shift[i]

            new_code = (((ord(s[i]) + cum_sum) - 97) % 26) + 97
            s = s[:i] + chr(new_code) + s[i+1:]
        
        return s
        
