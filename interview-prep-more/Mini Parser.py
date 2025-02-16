class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return NestedInteger()
        if s[0] != '[':
            return NestedInteger(int(s))
        if len(s) <= 2:
            return NestedInteger()
        start, cnt = 1, 0
        res = NestedInteger()
        for i in range(1, len(s)):
            if cnt == 0 and (s[i] == ',' or i == len(s) - 1):
                res.add(self.deserialize(s[start:i]))
                start = i + 1
            elif s[i] == '[':
                cnt += 1
            elif s[i] == ']':
                cnt -= 1
        return res
