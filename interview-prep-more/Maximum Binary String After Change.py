"""
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        loc = deque([i for i, x in enumerate(binary) if not int(x)])
        if not loc: return binary

        while len(loc) > 1:
            cur = loc.popleft()
            if loc:
                loc.popleft()
                loc.appendleft(cur+1)
        
        ans = ['1'] * len(binary)
        ans[loc.popleft()] = '0'
        return ''.join(ans)


class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        k = binary.find('0')
        if k == -1:
            return binary
        k += binary[k + 1 :].count('0')
        return '1' * k + '0' + '1' * (len(binary) - k - 1)


class Solution:
    def maximumBinaryString(self, binary):
        n, count = len(binary), 0

        ans = ["1"]*n

        for i in range(n):
            if binary[i] == "0":
                count += 1 

        for i in range(n):
            if binary[i] == "0":
                ans[i+count-1] = "0"
                return "".join(ans)

        return binary
"""

class Solution:
        def maximumBinaryString(self, s):
            if '0' not in s: return s
            k, n = s.count('1', s.find('0')), len(s)
            return '1' * (n - k - 1) + '0' + '1' * k
