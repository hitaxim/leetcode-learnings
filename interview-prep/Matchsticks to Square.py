class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        if sum(matchsticks) % 4 != 0:
            return False
        squ = sum(matchsticks) // 4
        sides = [0] * 4
        matchsticks.sort(reverse = True)

        def bt(i):
            if i == len(matchsticks):
                    return True
            
            for idx in range(4):
                if sides[idx] + matchsticks[i] <= squ:
                    sides[idx] += matchsticks[i]
                    if bt(i+1):
                        return True
                    sides[idx] -= matchsticks[i]
            return False
        
        return bt(0)
