class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create adjacency list
        adjacency = {i: [] for i in range(1, n + 1)}
        for src, dst, time in times:
            adjacency[src].append((dst, time))

        # Priority queue for Dijkstra's algorithm (min-heap based on time)
        pq = [(0, k)]  # (time, node)
        visited = set()
        delays = 0

        while pq:
            time, node = heapq.heappop(pq)

            # Skip if the node has been visited
            if node in visited:
                continue

            visited.add(node)
            delays = max(delays, time)

            for neighbor, neighbor_time in adjacency.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (time + neighbor_time, neighbor))

        # Check if all nodes have been visited
        return delays if len(visited) == n else -1
