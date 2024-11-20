class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        freq = [0] * 3
        size = len(s)

        for ch in s: 
            freq[ord(ch) - ord('a')] += 1
        
        l = 0
        r = 0

        if freq[0] < k or freq[1] < k or freq[2] < k:
            return -1
        
        for r in range(size):
            freq[ord(s[r]) - ord('a')] -= 1
        
            if freq[0] < k or freq[1] < k or freq[2] < k:
                freq[ord(s[l]) - ord('a')] += 1
                l += 1
        
        return size - (r - l + 1)
