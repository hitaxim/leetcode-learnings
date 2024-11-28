class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        count = sorted(Counter(word).values())

        prefix = 0
        suffix = sum(count)
        m = len(count)
        j = 0
        result = suffix

        for i, a in enumerate(count):
            while j < m and count[j] - a <= k:
                suffix -= count[j]
                j += 1
            current = prefix + suffix - (m - j) * (a + k)
            result = min(result, current)
            prefix += a
        
        return result
        
