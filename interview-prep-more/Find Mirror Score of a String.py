class Solution:
    def calculateScore(self, s: str) -> int:
        res = 0
        count = defaultdict(deque)
        for i, c in enumerate(s):
            cur_char = chr(ord("z") - ord(c) + ord("a"))
            if cur_char in count and count[cur_char]:
                res += i - count[cur_char].pop()
            else:
                count[c].append(i)
        return res
