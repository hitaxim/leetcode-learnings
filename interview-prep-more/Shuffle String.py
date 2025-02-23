class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(indices)
        x = [""] * n
        for i in range(n):
            x[indices[i]] = s[i]
        return "".join(x)

"""
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [""] * len(indices)
        for x, y in enumerate(indices):
            ans[y] = s[x]
        return "".join(ans)
"""
