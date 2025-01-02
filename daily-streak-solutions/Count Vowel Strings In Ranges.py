class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        prefix = [0]

        for w in words:
            curr = prefix[-1]
            if w[0] in vowels and w[-1] in vowels:
                curr += 1
            prefix.append(curr)
        
        res = []
        for l, r in queries:
            res.append(prefix[r + 1] - prefix[l])
        return res
