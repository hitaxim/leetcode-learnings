class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_counts = {}
        for row in wall:
            edge_pos = 0
            for brick_width in row[:-1]:
                edge_pos += brick_width
                edge_counts[edge_pos] = edge_counts.get(edge_pos, 0) + 1
        return len(wall) - max(edge_counts.values(), default=0)
