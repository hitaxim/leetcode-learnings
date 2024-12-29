class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        p_land = set()
        a_land = set()

        r, c = len(heights), len(heights[0])

        def spread(i, j, land):
            land.add((i, j))
            dirs = ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1))
            for x, y in dirs:
                if (
                    0 <= x < r
                    and 0 <= y < c
                    and heights[x][y] >= heights[i][j]
                    and (x, y) not in land
                ):
                    spread(x, y, land)
        
        for i in range(r):
            spread(i, 0, p_land)
            spread(i, c - 1, a_land)
        for j in range(c):
            spread(0, j, p_land)
            spread(r-1, j, a_land)

        return list(p_land & a_land)
