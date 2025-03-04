class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        def check_direction(R,C,direction):
            if direction=="right":
                for col in range(C+1,8): # increasing col 
                    if board[R][col].islower():return 1
                    if board[R][col].isupper():return 0
            if direction=="left":
                for col in range(C-1,-1,-1): # decreasing col 
                    if board[R][col].islower():return 1
                    if board[R][col].isupper():return 0
            if direction=="down":
                for row in range(R+1,8): # increasing row
                    if board[row][C].islower():return 1
                    if board[row][C].isupper():return 0
            if direction=="up": 
                for row in range(R-1,-1,-1): # decreasing col 
                    if board[row][C].islower():return 1
                    if board[row][C].isupper():return 0
            return 0 # we reach the edge (nothing was found)
                    
        for row in range(8):
            for col in range(8):
                if board[row][col]=="R":
					# sum all directions up
                    return sum([check_direction(row,col,"right"),
                                check_direction(row,col,"left"),
                                check_direction(row,col,"up"),
                                check_direction(row,col,"down")])
