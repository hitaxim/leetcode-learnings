class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballColor = {} # ball:color
        colorBalls = defaultdict(set) # color:balls
        res = []

        for ball, color in queries:
            if ball in ballColor:
                oldColor = ballColor[ball]
                colorBalls[oldColor].remove(ball)
                if not colorBalls[oldColor]:
                    del colorBalls[oldColor]
            
            ballColor[ball] = color
            colorBalls[color].add(ball)
            res.append(len(colorBalls))
        
        return res
        
