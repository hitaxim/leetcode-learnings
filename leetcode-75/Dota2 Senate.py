from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_q = deque()
        dire_q = deque()

        for i, val in enumerate(senate):
            if val == "R":
                radiant_q.append(i)
            else: 
                dire_q.append(i)

        while radiant_q and dire_q: 
            radiant_idx = radiant_q.popleft()
            dire_idx = dire_q.popleft()

            if radiant_idx < dire_idx: 
                radiant_q.append(radiant_idx + len(senate))
            else: 
                dire_q.append(dire_idx + len(senate))

        return "Radiant" if radiant_q else "Dire"
