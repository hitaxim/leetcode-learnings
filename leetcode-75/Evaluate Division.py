class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (a,b), value in zip(equations, values):
            if a not in graph: 
                graph[a] = {}
            if b not in graph: 
                graph[b] = {}
            graph[a][b] = value
            graph[b][a] = 1/value
        
        def dfs(src, dst, visited):
            if src not in graph or dst not in graph: 
                return -1.0
            if src == dst: 
                return 1.0
            visited.add(src)
            for neighbor, val in graph[src].items(): # gets the neigh and value for its dictionary items
                if neighbor in visited: 
                    continue
                result = dfs(neighbor, dst,visited)
                if result != -1.0:
                    return result * val
            return -1.0

        results = []
        for q in queries: 
            results.append(dfs(q[0],q[1], set()))
        return results
