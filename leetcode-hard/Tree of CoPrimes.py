lass Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        indices = [[] for _ in range(max(nums) + 1)]
        adj = [[] for _ in range(len(nums))]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        ans = [-1] * len(nums)

        def dfs(u, h, p):
            best_h = -1
            best_a = -1
            for x in range(1, len(indices)):
                if indices[x] and best_h < indices[x][-1][0] and gcd(x, nums[u]) == 1: 
                    best_h, best_a = indices[x][-1]
            
            ans[u] = best_a
            indices[nums[u]].append((h,u))

            for v in adj[u]:
                if v == p:
                    continue
                dfs(v, h+1, u)
            
            indices[nums[u]].pop()
        
        dfs(0, 0, -1)
        return ans
        
