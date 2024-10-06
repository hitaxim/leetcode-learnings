class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 0: 
            return 0
        q = deque([n])
        visited = set([n])
        level = 0
        while q: 
            level += 1
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                for i in range(1, int(curr**0.5) +1):
                    rem = curr - i * i
                    if rem == 0:
                        return level 
                    if rem not in visited:
                        q.append(rem)
                        visited.add(rem)
        return level
        
