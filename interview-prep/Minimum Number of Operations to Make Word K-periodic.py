class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        mp = {}
        n = len(word)
        for i in range(0, n, k):
            tmp = word[i:i+k]
            mp[tmp] = mp.get(tmp, 0) + 1
        
        mx = max(mp.values()) if mp else 0
        result = (n // k) - mx
        return result
  
