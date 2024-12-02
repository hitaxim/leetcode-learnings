class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        # negate to create a max-heap
        cuts = [(-cost, "H") for cost in horizontalCut] + [(-cost, "V") for cost in verticalCut]
        heapq.heapify(cuts)

        h_p = 1
        v_p = 1
        
        total_cost = 0

        while cuts:
            cost, cut_type = heapq.heappop(cuts)
            cost = -cost

            if cut_type = "H":
                h_p += 1
                total_cost += cost * v_p
            else: 
                v_p += 1
                total_cost += cost * h_p
                
        return total_cost
