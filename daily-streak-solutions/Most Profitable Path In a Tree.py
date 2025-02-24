from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        bobPath = {}
        visited = set()
        def findBobPath(node, time):
            visited.add(node)
            bobPath[node] = time
            if node == 0:
                return True
            for nei in adj[node]:
                if nei not in visited and findBobPath(nei, time + 1):
                    return True
            bobPath.pop(node)
            return False
        
        findBobPath(bob, 0)
        visited.clear()
        maxProfit = float('-inf')
        
        def findAlicePath(node, time, income):
            nonlocal maxProfit
            visited.add(node)
            if node not in bobPath or time < bobPath[node]:
                income += amount[node]
            elif time == bobPath[node]:
                income += amount[node] // 2
            
            if len(adj[node]) == 1 and node != 0:
                maxProfit = max(maxProfit, income)
            
            for nei in adj[node]:
                if nei not in visited:
                    findAlicePath(nei, time + 1, income)
        
        findAlicePath(0, 0, 0)
        return maxProfit
