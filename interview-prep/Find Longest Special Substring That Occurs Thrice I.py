class Solution:
    def maximumLength(self, s: str) -> int:
        mps = defaultdict(int)
        count = 0

        for i in range(len(s)):
            count = 1
            mps[(s[i], count)] += 1

            for j in range(i, len(s)):
                if j + 1 < len(s) and s[j] == s[j+1]:
                    count += 1
                    mps[(s[i], count)] += 1
                else:
                    break

        ans = 0
        for key, val in mps.items(): 
            if val >= 3: 
                ans = max(ans ,key[1])
                
        return ans if ans != 0 else -1
