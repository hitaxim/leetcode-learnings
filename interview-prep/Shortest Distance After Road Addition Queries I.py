class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for i in range(n-1):
            graph[i].append(i+1)
        
        def bfs(graph):
            queue = deque([0])
            seen = {0}
            ans = 0
            while queue:
                for _ in range(len(queue)):
                    u = queue.popleft()
                    if u == n - 1: return ans
                    for v in graph[u]:
                        if v not in seen:
                            seen.add(v)
                            queue.append(v)
                ans += 1
        
        ans = []
        for u, v in queries: 
            graph[u].append(v)
            ans.append(bfs(graph))
        return ans
