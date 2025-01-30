class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        s = self.countAndSay(n - 1)
        result = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result.append(str(count) + s[i - 1])
                count = 1
        result.append(str(count) + s[-1])
        return "".join(result)
