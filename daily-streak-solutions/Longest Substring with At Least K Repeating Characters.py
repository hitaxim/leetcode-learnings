class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        q = ''.join(c for c,f in Counter(s).items() if f<k)
        if q:
            return max(self.longestSubstring(t, k) for t in split(f'[{q}]', s))
        else:
            return len(s)
