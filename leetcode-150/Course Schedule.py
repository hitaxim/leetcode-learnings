class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        ans = []

        for p in prerequisites:
            course = p[0]
            prereq = p[1]
            adj[prereq].append(course)
            indegree[course] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0: 
                q.append(i)
        
        while q:
            curr = q.popleft()
            ans.append(curr)

            for next_c in adj[curr]:
                indegree[next_c] -= 1
                if indegree[next_c] == 0:
                    q.append(next_c)

        return len(ans) == numCourses
