class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        visited = [0] * len(graph)
   
        def has_cycle(node):
            if visited[node] == -1:
                return True
            if visited[node] == 1:
                return False
            visited[node] = -1
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            visited[node] = 1
            return False

        return [node for node in range(len(graph)) if not has_cycle(node)]

"""
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        seen = set()
        ans = []

        def dfs(i: int) -> bool:
            if graph[i] == []:
                return True
            if i in seen:
                return False
            
            seen.add(i)
            for node in graph[i]:
                if not dfs(node):
                    return False
            
           
            graph[i] = []
            return True

        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)

        return ans
"""
