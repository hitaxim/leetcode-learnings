class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s: 
            return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                for strs in self.partition(s[i:]):
                    ans.append([s[:i]] + strs)
        return ans
