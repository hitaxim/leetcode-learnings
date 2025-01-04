class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        d = defaultdict(list)
        for i, val in enumerate(s):
            d[val].append(i)
        
        ans = 0
        for el in d:
            if len(d[el]) < 2:
                continue
            a = d[el][0]
            b = d[el][-1]
            ans += len(set(s[a+1:b]))
            
        return (ans)
