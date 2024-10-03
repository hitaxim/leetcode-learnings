class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in sorted(tickets, reverse= True):
            graph[src].append(dst)

        ans = []
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            ans.append(airport)
        
        dfs("JFK")
        return ans[::-1]
