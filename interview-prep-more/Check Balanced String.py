class Solution:
    def isBalanced(self, num: str) -> bool:
        it, ans = iter(num), 0
        while ((even := next(it, None)) is not None):
            ans += int(even) - (odd := int(next(it, 0)))
        return not ans
