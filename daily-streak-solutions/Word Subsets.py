class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        maxFreq = {}
        for w in words2:
            for c, n in Counter(w).items():
                if c not in maxFreq or maxFreq[c] < n:
                    maxFreq[c] = n
        
        res = []
        for word in words1:
            universal = True
            count = Counter(word)
            for c, n in maxFreq.items():
                if c not in count or n > count[c]:
                    universal = False
                    break 
            if universal : res.append(word)
        
        return res

        
