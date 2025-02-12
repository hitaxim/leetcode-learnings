class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:

        seen = set()

        def dfs(tot):
            if tot == targetCapacity:
                return True
            if tot in seen or tot < 0 or tot > jug1Capacity + jug2Capacity:
                return False
            
            seen.add(tot)

            return dfs(tot+jug1Capacity) or dfs(tot-jug1Capacity) or dfs(tot+jug2Capacity) or dfs(tot-jug2Capacity)
        
        return dfs(0)

"""
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        
        q = deque([0])
        seen = set()
        steps = [jug1Capacity, -jug1Capacity, jug2Capacity, -jug2Capacity]

        while q:
            cur = q.popleft()
            for step in steps:
                tot = cur + step 
                if tot == targetCapacity:
                    return True
                if tot not in seen and 0 <= tot <= jug1Capacity + jug2Capacity:
                    seen.add(tot)
                    q.append(tot)
        return False
"""
