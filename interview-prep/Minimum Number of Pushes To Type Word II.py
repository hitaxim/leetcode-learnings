class Solution:
    def minimumPushes(self, word: str) -> int:
        count = {}
        for c in word:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        
        charCount = sorted(list(count.items()), key = lambda a: -a[1])
        left = 8
        cost = 1
        res = 0
        for item in charCount : 
            char, count = item
            res += cost * count
            left -= 1
            if left == 0:
                left = 8
                cost += 1
        return res
