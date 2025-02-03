
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.recurse(s, ans, 0, "", 0)
        return ans
    
    def recurse(self, curr, ans, index, temp, count):
        if count > 4:
            return
        if count == 4 and index == len(curr):
            ans.append(temp)
        for i in range(1, 4):
            if index + i > len(curr):
                break
            s = curr[index:index+i]
            if (s.startswith("0") and len(s) > 1) or (i == 3 and int(s) >= 256):
                continue
            self.recurse(curr, ans, index+i, temp + s + ("." if count < 3 else ""), count+1)


"""
class Solution:
    def valid(self, temp: str) -> bool:
        if len(temp) > 3 or len(temp) == 0:
            return False
        if len(temp) > 1 and temp[0] == '0':
            return False
        if len(temp) and int(temp) > 255:
            return False
        return True

    def solve(self, ans, output, ind, s, dots):
        if dots == 3:
            if self.valid(s[ind:]):
                ans.append(output + s[ind:])
            return
        for i in range(ind, min(ind+3, len(s))):
            if self.valid(s[ind:i+1]):
                new_output = output + s[ind:i+1] + '.'
                self.solve(ans, new_output, i+1, s, dots+1)

    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.solve(ans, "", 0, s, 0)
        return ans

"""
