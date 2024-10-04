class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        c_1 = Counter(word1)
        c_2 = Counter(word2)
        if set(c_1.keys()) != set(c_2.keys()):
            return False
        a = list(c_1.values())
        b = list(c_2.values())
        a.sort()
        b.sort()
        return a == b
