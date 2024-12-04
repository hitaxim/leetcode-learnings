class Solution:
  def canMakeSubsequence(self, A: str, B: str) -> bool:
    bi, lenA, lenB = 0, len(A), len(B)

    for ai in range(lenA):
      if bi < lenB and (ord(B[bi]) - ord(A[ai])) % 26 < 2:
        bi += 1

    return bi == lenB
    
        
