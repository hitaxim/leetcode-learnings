class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        edges = set()
        for src, dest in connections:  # Adding the edges and neighbor list for nodes
            edges.add((src,dest))
            graph[src].append(dest)
            graph[dest].append(src)
        
        visited = {0}
        res = 0

        def dfs(city):
            nonlocal graph, edges, visited, res
            for n in graph[city]: # getting the neighbors
                if n in visited: 
                    continue
                if (n,city) not in edges: 
                    res += 1
                visited.add(n)
                dfs(n)

        dfs(0)
        return res

"""
Example 1: 
0 -> 1 (need to change)
1 -> 3 (need to change)
2 -> 3 
4 -> 0 
4 -> 5 (need to change)

Example 2: 
1 -> 0 
1 -> 2 (need to change)
3 -> 2 
3 -> 4 (need to change)

Example 3: 
1 -> 0
2 -> 0
"""   
