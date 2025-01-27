"""
import re
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = dict(knowledge)
        s = s.replace('(','(*')
        ss = re.findall(r'[^()]+',s)
        #print(ss)
        n = len(ss)
        for i in range(n):
            if  ss[i][0] !='*':continue
            cur = ss[i][1:]
            if cur in d: ss[i]= d[cur]
            else: ss[i]='?'

        return ''.join(ss)
"""

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:

        d = dict((itm[0] , itm[1]) for itm in knowledge )

        new = ''
        cur = ''
        b = 0

        i = 0
        while i < len(s):
            if s[i] == '(':
                i += 1
                while s[i] != ')':
                    cur += s[i]
                    i += 1
                if cur in d:
                    new += d[cur]
                else:
                    new += '?'
                cur = ''
            else:
                new += s[i]
            i += 1

        return new
           
