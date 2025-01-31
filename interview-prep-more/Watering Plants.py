class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        can = capacity
        for i, x in enumerate(plants): 
            if can < x: 
                ans += 2*i
                can = capacity
            ans += 1
            can -= x
        return ans 

"""
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cap = capacity
        steps = 0
        n = len(plants)
        for i in range(n):
            if plants[i] > cap:
                steps += 2*i +1
                cap = capacity - plants[i]
            elif plants[i] < cap:
                cap -= plants[i]
                steps += 1
            else:
                cap = 0
                steps += 1
        return steps
"""
