class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        trie = Trie()
        for w in words:
            trie.insert(w)
        
        n = len(target)
        dp = [-1] * n

        def dfs(i):
            if i == n: 
                return 0
            if dp[i] != -1 : 
                return dp[i]
            
            res = float('inf')
            cur = trie
            for j in range(i, n):
                if target[j] not in cur.children:
                    break
                cur = cur.children[target[j]]
                res = min(res, 1 + dfs(j + 1))
            
            dp[i] = res
            return res
        
        result = dfs(0)
        return result if result != float('inf') else -1

class Trie: 
    def __init__(self):
        self.children = {}

    def insert(self, s):
        cur = self
        for c in s:
            if c not in cur.children: 
                cur.children[c] = Trie()
            cur = cur.children[c]
