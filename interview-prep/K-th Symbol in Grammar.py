class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        # start with 0
            # 0 turns 01
            # 1 turns 10

        # if k is odd, get 0th from the cur str
        stack = [0 if k % 2 else 1] 

        while n > 1:
            k = (k + 1) // 2
            stack.append(0 if k % 2 else 1)
            n -= 1
        
        cur = "0"
        while stack:
            idx = stack.pop()
            cur = "01" if cur == "0" else "10"
            cur = cur[idx]
        
        return int(cur)
