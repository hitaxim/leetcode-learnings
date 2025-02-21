lass Solution:
    def winnerOfGame(self, colors: str) -> bool:

        alice = 0
        bob = 0

        for i in range(1, len(colors)-1):

            if colors[i-1] == colors[i] == colors[i+1]:

                if colors[i] == "A":
                    alice +=1
                else:
                    bob +=1        
        
        if alice > bob:
            return True
        return False

"""
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        c = collections.Counter()
        for x, t in groupby(colors):
            c[x] += max(len(list(t)) - 2, 0)
        if c['A'] > c['B']:
            return True
        return False
"""
