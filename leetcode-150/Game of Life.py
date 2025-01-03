class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rowLen=len(board[0])
        colLen=len(board)
        ans = [[-1 for x in range(rowLen)] for y in range(colLen)]

        def inBound(i,j):
            return (0<=i<colLen) and (0<=j<rowLen)

        for i in range(colLen):
            for j in range(rowLen):
                count=0
                for ii,jj in [(i,j+1),(i,j-1),(i-1,j),(i+1,j),(i-1,j+1),(i+1,j-1),(i+1,j+1),(i-1,j-1)]:
                    if inBound(ii,jj):
                        count+=board[ii][jj]
                if count<2:
                    ans[i][j]=0
                elif board[i][j]==1 and (count==2 or count==3):
                    ans[i][j]=1
                elif board[i][j]==1 and count>3:
                    ans[i][j]=0
                elif board[i][j]==0 and count==3:
                    ans[i][j]=1
                else:
                    ans[i][j]=board[i][j]

        board[:]=ans
        return board
                
        
