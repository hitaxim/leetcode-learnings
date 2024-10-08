class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        # Build graph
        for course, prereq in prerequisites: 
            graph[prereq].append(course)
        # Calculate in-degree
        in_degree = [0] * numCourses
        for c, p in prerequisites : 
            in_degree[c] += 1
        
        # Perform Topological sort
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        result = []
        while queue: 
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check cycle: 
        if len(result) < numCourses:
            return []

        return result        
