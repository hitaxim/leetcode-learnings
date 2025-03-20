class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, w))

        def dfs(x: int) -> int:
            and_ = -1
            ids[x] = len(cc_and)
            for y, w in g[x]:
                and_ &= w
                if ids[y] < 0:
                    and_ &= dfs(y)
            return and_

        ids = [-1] * n
        cc_and = []
        for i in range(n):
            if ids[i] < 0:
                cc_and.append(dfs(i))

        return [0 if s == t else -1 if ids[s] != ids[t] else cc_and[ids[s]]
                for s, t in query]
