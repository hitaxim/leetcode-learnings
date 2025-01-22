class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return [word for word in words
                if len(word) == len(pattern) and
                len(set(word)) == len(set(pattern)) and
                len(set(zip(word, pattern))) == len(set(word))]

"""
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for i in words:
            a = {}
            b = {}
            for j in range(len(i)):
                if i[j] not in a:
                    a[i[j]] = [j]
                else:
                    a[i[j]].append(j)

                if pattern[j] not in b:
                    b[pattern[j]] = [j]
                else:
                    b[pattern[j]].append(j)
            if list(b.values()) == list(a.values()):
                res.append(i)
        return res
"""
