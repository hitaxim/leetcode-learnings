class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        
        maxTime = logs[0][1]
        res = logs[0][0]

        for i in range(1, len(logs)):
            taskDuration = logs[i][1] - logs[i-1][1]
            if taskDuration > maxTime or (taskDuration == maxTime and logs[i][0] < res):
                res = logs[i][0]
                maxTime = taskDuration
        return res

"""
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        prev, ans = 0, (0,0)

        for id, curr in logs:
            ans = min(ans, (prev-curr, id))
            prev = curr

        return ans[1]

"""
        
