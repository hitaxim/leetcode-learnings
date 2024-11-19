class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        adj = defaultdict(list)
        for a, b, w in edges: 
            adj[a].append((b,w))
            adj[b].append((a, w))

        @cache
        def dfs(node, parent, path):
            connectable = 1 if path == 0 else 0
            for neigh, w in adj[node]:
                if neigh == parent: 
                    continue
                connectable += dfs(neigh, node, (path + w) % signalSpeed)
            return connectable
    
        ans = [0] * n
        for root in range(n):
            branches = adj[root]

            for i in range(len(branches)):
                a, awt = branches[i]
                for j in range(i+1, len(branches)):
                    b, bwt = branches[j]
                    ans[root] += dfs(a, root, awt % signalSpeed) * dfs(b, root, bwt % signalSpeed)
        return ans
