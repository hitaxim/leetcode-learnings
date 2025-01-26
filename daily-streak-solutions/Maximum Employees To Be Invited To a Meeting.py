class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        in_degree = [0] * n
        
        # Calculate in-degree for each node
        for person in range(n):
            in_degree[favorite[person]] += 1
        
        # Topological sorting to remove non-cycle nodes
        q = deque()
        for person in range(n):
            if in_degree[person] == 0:
                q.append(person)
        
        depth = [1] * n  # Depth of each node
        
        while q:
            current_node = q.popleft()
            next_node = favorite[current_node]
            depth[next_node] = max(depth[next_node], depth[current_node] + 1)
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                q.append(next_node)
        
        longest_cycle = 0
        two_cycle_invitations = 0
        
        # Detect cycles
        for person in range(n):
            if in_degree[person] == 0:  # Already processed
                continue
            
            cycle_length = 0
            current = person
            while in_degree[current] != 0:
                in_degree[current] = 0  # Mark as visited
                cycle_length += 1
                current = favorite[current]
            
            if cycle_length == 2:
                # For 2-cycles, add the depth of both nodes
                two_cycle_invitations += depth[person] + depth[favorite[person]]
            else:
                longest_cycle = max(longest_cycle, cycle_length)
        
        return max(longest_cycle, two_cycle_invitations)

"""
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        adj=defaultdict(list)
        transpose=defaultdict(list)
        #first we apply kosaraju, its a cycle, it is that answer itself
        #or we can combine multiple 2 sized connected components (if 0's fav is 1 and 1s fav is 0) ->one exception case to consider
        #max of both the above conditions
        for i in range(len(favorite)):
            adj[i].append(favorite[i])
            transpose[favorite[i]].append(i)
        
        stack=[]
        visited=[False]*len(favorite)
        def dfs(node):
            visited[node]=True
            for n in adj[node]:
                if not visited[n]:
                    dfs(n)
            stack.append(node)
        
        for i in range(len(favorite)):
            if not visited[i]:
                dfs(i)
        
        sccs=[] #list of sets of each scc
        scc=set()
        visited=[False]*len(favorite)
        def traverseForScc(node):
            visited[node]=True
            scc.add(node)
            for n in transpose[node]:
                if not visited[n]:
                    traverseForScc(n)
        
        while stack:
            top = stack.pop()
            if not visited[top]:
                scc = set()
                traverseForScc(top)
                sccs.append(scc)
        
        ans=max([len(scc) if len(scc)!=2 else -1 for scc in sccs])
        #above was from kosaraju

        def findLongestArm(a,b):
            l=0
            for node in transpose[a]:
                if node!=b:
                    l=max(l,1+findLongestArm(node,b))
            return l

        twoNodeSccs = 0
        for n1,n2 in [scc for scc in sccs if len(scc)==2]:
            twoNodeSccs+= 2 + findLongestArm(n1,n2) + findLongestArm(n2,n1)
        return max(ans,twoNodeSccs)
"""
