class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # from the back to the need
        n = len(A)
        ans = collections.deque()
        
        seen = set()
        idx = n - 1
        while idx >= 0:
            ans.appendleft(n - len(seen))
            seen.add(A[idx])
            seen.add(B[idx])
            idx -= 1
        
        return list(ans)
            
