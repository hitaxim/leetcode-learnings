class Solution:
    def punishmentNumber(self, n: int) -> int:
        s = 0

        def dfs(s, start_idx, num_left, n):
            if start_idx == n and num_left == 0:
                return True
            elif num_left < 0:
                return False
            
            left_num = 0
            for i in range(start_idx, n):
                left_num = left_num * 10 + int(s[i])
                if dfs(s, i + 1, num_left - left_num, n):
                    return True
            
            return False


        for i in range(1, n + 1):
            squaredI = i * i
            s += squaredI if dfs(str(squaredI), 0, i, len(str(squaredI))) else 0
            
        return s

"""
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(x, target):
            if x==target: return True
            if x==0: return target==0
            for m in (10, 100, 1000):
                if partition(x//m, target-x%m):
                    return True
            return False
        return sum(x for i in range(1, n+1) if partition(x:=i*i, i))
       
"""
