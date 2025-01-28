class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        locs = defaultdict(list)
        for i, ch in enumerate(s): locs[ch].append(i)
        
        @cache
        def fn(lo, hi):
            """Return count of palindromic subsequences in s[lo:hi]."""
            if lo == hi: return 0
            ans = 0 
            for ch in "abcd": 
                i = bisect_left(locs[ch], lo)
                j = bisect_left(locs[ch], hi) - 1
                if i <= j < len(locs[ch]) and lo <= locs[ch][i] <= locs[ch][j] < hi: 
                    ans += 1
                    if i < j: ans += 1 + fn(locs[ch][i]+1, locs[ch][j])
            return ans % 1_000_000_007
        
        return fn(0, len(s))
