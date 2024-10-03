class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row = len(maze)
        col = len(maze[0])

        ways = deque()
        ways.append((entrance[0], entrance[1],0))
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while ways: 
            for _ in range(len(ways)):
                pos_x, pos_y, level  = ways.popleft()
                if [pos_x, pos_y] != entrance:
                    if pos_x == 0 or pos_x == row - 1 or pos_y == 0 or pos_y == col -1 :
                        return level

                for xx, yy in [(pos_x,pos_y+1),(pos_x,pos_y-1),(pos_x+1,pos_y), (pos_x-1,pos_y)]:
                     

                    if 0 <= xx < row and 0 <= yy < col and (xx, yy) not in visited and maze[xx][yy] == ".":
                        ways.append((xx,yy,level +1))
                        visited.add((xx,yy))
        return -1
    
"""
. empty
+ wall
e (r, c)
"""
