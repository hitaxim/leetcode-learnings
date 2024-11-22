class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        sig_count = defaultdict(int)

        for row in matrix:
            # list for mutable, unsuitable for key, so we use typle as it is inmutable
            if row[0] == 1:
                pattern = tuple(row)
            else:
                pattern = tuple(1 - val for val in row)
            
            sig_count[pattern] += 1
        
        return max(sig_count.values())

"""
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        groups = defaultdict(int)
        for r in matrix: 
            row = tuple(r)
            inverse = tuple(1 - bit for bit in row)
            groups[row] += 1
            groups[inverse] += 1
        return max(groups.values())
"""
