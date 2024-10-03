class Solution:
    def partitionString(self, s: str) -> int:
        n_s = 1

        visited = set()
        for x in s:
            if x not in visited: 
                visited.add(x)
                continue
            else: 
                visited.clear()
                visited.add(x)
                n_s += 1
        return n_s
