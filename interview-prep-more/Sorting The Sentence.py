class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split()
        lst = sorted(lst,key=lambda x:x[-1])
        return ' '.join([st[:-1] for st in lst])
