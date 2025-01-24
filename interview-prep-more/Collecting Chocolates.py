class Solution:
    def minCost(self, A: List[int], X: int) -> int:
        ans = sum(A)
        for rotations in range(1, len(A)):
            A = [min(A[i], A[i-1]) for i in range(len(A))]
            ans = min(ans, rotations * X + sum(A))
        return ans
