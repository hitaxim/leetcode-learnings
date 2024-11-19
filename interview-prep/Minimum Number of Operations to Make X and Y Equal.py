class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        
        if y >= x:
            return y-x
        
        max_x = x + 11
        q = deque()
        q.append((x, y, 0))

        vis = [False] * (x+12)
        vis[x] = True

        while q:
            x, y, cnt = q.popleft()
            
            if x == y:
                return cnt
            
            if x % 11 == 0 and not vis[x//11]:
                vis[x//11] = True
                q.append((x//11, y, cnt+1))

            if x % 5 == 0 and not vis[x//5]:
                vis[x//5] = True
                q.append((x//5, y, cnt+1))

            if x > 1 and not vis[x-1]:
                vis[x-1] = True
                q.append((x-1, y, cnt+1))

            if x < max_x and not vis[x+1]:
                vis[x+1] = True
                q.append((x+1, y, cnt+1))

        return 0
