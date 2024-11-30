class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n, res = len(s), []

        for i in range(n):
            str1, c_c, c_v = s[i], 0, 0

            if s[i] in "aeiou":
                c_v += 1
            else:
                c_c += 1

            for j in range(i+1, n):
                if s[j] in "aeiou":
                    c_v += 1
                else: 
                    c_c += 1
                str1 += s[j]
                
                if c_v == c_c and (c_c * c_v) % k == 0:
                    res.append(str1)
        
        return len(res)
