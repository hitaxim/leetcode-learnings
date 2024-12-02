class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        ans = []
        for i in range(len(words)-1, -1, -1):
            ans.append(words[i])

        return " ".join(ans)
