class Solution:
    def dfs(self, graph, node, visit):
        visit.add(node)
        for nei in graph[node]:
            if nei not in visit:
                self.dfs(graph, nei, visit)
        self.res.append(node)
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        for account in accounts:
            for email in account[1:]:
                graph[account[1]].add(email)
                graph[email].add(account[1])
        #print(graph.items())
        
        visit = set()
        ans = []
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in visit:
                    self.res = []
                    self.dfs(graph, email, visit)
                    ans.append([name]+sorted(self.res))
        return ans
"""
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        for acc in accounts:
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
        
        res = []
        visit = set()

        for acc in accounts:
            if acc[1] not in visit:
                name = acc[0]
                stack = [acc[1]]
                emails = []
                while stack:
                    node = stack.pop()
                    if node not in visit:
                        visit.add(node)
                        stack.extend(graph[node])
                        emails.append(node)

                res.append([name] + sorted(emails))
        return res
"""
