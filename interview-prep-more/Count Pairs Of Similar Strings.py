class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans = 0
        freq = defaultdict(int)

        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << ord(c) - ord('a')
            ans += freq[mask]
            freq[mask] += 1

        return ans

