class neighborSum:

    def __init__(self, grid: List[List[int]]):

        self.indices = defaultdict(tuple)
        self.values  = defaultdict(int)

        for i, j in product(range(len(grid)), range(len(grid[0]))):
            self.values[(i,j)] = grid[i][j]
            self.indices[grid[i][j]] = (i,j)

    def adjacentSum(self, value: int, sm = 0) -> int:

        i, j = self.indices[value]
        for I, J in ((i-1, j),(i+1, j),(i, j-1), (i, j+1)):
            if (I,J) in self.values: sm+= self.values[(I,J)]

        return sm    

    def diagonalSum(self, value: int, sm = 0) -> int:
        
        i, j = self.indices[value]
        for I, J in ((i-1, j-1), (i+1, j-1), (i-1, j+1), (i+1, j+1)):
            if (I,J) in self.values: sm+= self.values[(I,J)]
        
        return sm
