class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        rowcount = 0
        colcount = 0
        total = 0
        rowSeen = [False] * n 
        colSeen = [False] * n
        
        for q in range(len(queries)-1, -1, -1):
            typei, idx, val = queries[q][0], queries[q][1], queries[q][2]
            if typei == 0 and not rowSeen[idx]:
                rowcount += 1
                rowSeen[idx] = True
                total += (n - colcount) * val 
            if typei == 1 and not colSeen[idx]:
                colcount += 1
                colSeen[idx] = True 
                total += (n - rowcount) * val 

        return total 
