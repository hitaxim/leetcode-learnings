class Solution:
    def oddString(self, words: List[str]) -> str:
        res = []
        for word in words:
            diff = [ord(word[i + 1]) - ord(word[i]) for i in range(len(word) - 1)]
            res.append(diff)

        for diff in res:
            if res.count(diff) == 1:
                return words[res.index(diff)]

