class Solution:
    def dfs(self, network, visited, srcComputer):
        visited[srcComputer] = True
        for adjComputer in network[srcComputer]:
            if not visited[adjComputer]:
                self.dfs(network, visited, adjComputer)
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        network = [[] for i in range(n)]
        for connection in connections:
            network[connection[0]].append(connection[1])
            network[connection[1]].append(connection[0])
        
        visited = [False] * n
        minOperations = 0
        for computer in range(n):
            if not visited[computer]:
                self.dfs(network, visited, computer)
                minOperations += 1
        
        return minOperations - 1
