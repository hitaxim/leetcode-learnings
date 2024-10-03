class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            visited.add(i)
            for j in range(n):
                if i!=j and isConnected[i][j] == 1 and j not in visited :
                    dfs(j)

        n = len(isConnected)
        n_prov = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                n_prov += 1
                dfs(i)

        return n_prov

ORRRRRR 
## CAN USE visited = [False] * n 
