class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0 
        vals = [-1]
        for i, ch in enumerate(s): 
            one = zero = 0
            if ch == '1': one += 1
            else: zero += 1
            p = i 
            for v in reversed(vals): 
                one += p-v-1
                ans += max(0, min(p-v, one-zero**2+1))
                p = v 
                zero += 1
                if zero**2 > i: break 
            if ch == '0': vals.append(i)
        return ans 

"""
class Solution(object):
    def numberOfSubstrings(self, s):
        result = 0
        last_zero_indices = [-1]
        n = len(s)

        for i in range(n):
            ch = s[i]
            count_ones = count_zeros = 0
            
            if ch == '1':
                count_ones += 1
            else:
                count_zeros += 1
            
            p = i
            
            for v in reversed(last_zero_indices):
                count_ones += p - v - 1
                result += max(0, min(p - v, count_ones - count_zeros**2 + 1))
                p = v
                count_zeros += 1
                if count_zeros**2 > i:
                    break
            
            if ch == '0':
                last_zero_indices.append(i)
        
        return result
"""
