class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        ans = [-1.0] * n
        stack = [] # keep track of cars and speed

        for i in range(n - 1, -1, -1):
            position, speed = cars[i]

            # Remove cars that are faster and never be collided 
            while stack and (cars[stack[-1]][1] >= speed or (cars[stack[-1]][0] - position)/(speed - cars[stack[-1]][1]) >= ans[stack[-1]] >= 0):
                stack.pop()
            
            # calculate collision time
            if stack:
                ans[i] = (cars[stack[-1]][0] - position)/(speed - cars[stack[-1]][1])
            # add current car
            stack.append(i)
        
        return ans

"""
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        ans = [-1.0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and cars[i][1] <= cars[stack[-1]][1]:
                stack.pop()
            
            while stack:
                time = (cars[stack[-1]][0] - cars[i][0]) / (cars[i][1] - cars[stack[-1]][1])
                if time <= ans[stack[-1]] or ans[stack[-1]] == -1.0:
                    ans[i] = time
                    break
                stack.pop()
            
            stack.append(i)
        
        return ans

"""
