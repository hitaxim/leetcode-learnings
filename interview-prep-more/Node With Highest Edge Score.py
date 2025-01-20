"""
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n, ans = len(edges), 0
        scores = [0] * n
        for src, tgt in enumerate(edges):
            scores[tgt] += src
        for i, score in enumerate(scores):
            if score > scores[ans]:
                ans = i
        return ans

"""
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        scores = [0] * n
        
        for i in range(n):
            scores[edges[i]] += i
        
        max_score = max(scores)
        
        
        for i in range(n):
            if scores[i] == max_score:
                return i
