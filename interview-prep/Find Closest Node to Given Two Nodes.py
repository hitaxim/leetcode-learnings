class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        visited1 = set()
        visited2 = set()

        while node1 != -1 or node2 != -1: 
            if node1 != -1 and node1 not in visited1: 
                if node1 in visited2: 
                    if node2 in visited1: 
                        return min(node1, node2)
                    return node1
                visited1.add(node1)
                node1 = edges[node1]

            
            if node2 != -1 and node2 not in visited2: 
                if node2 in visited1: 
                    return node2
                visited2.add(node2)
                node2 = edges[node2]
            if (node1 in visited1 or node1 == -1) and (node2 in visited2 or node2 == -1):
                break
        return -1
        
