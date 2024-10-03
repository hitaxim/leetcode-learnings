class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        keys = [0]
        visited[0] = True
        count = 1

        while keys: 
            key = keys.pop()
            for i in rooms[key]:
                if not visited[i]: 
                    keys.append(i)
                    visited[i] = True
                    count += 1

        return len(rooms) == count
