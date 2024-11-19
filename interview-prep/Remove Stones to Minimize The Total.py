class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        # Construct frequency table
        count = [0 for x in range(max(piles)+1)]
        for x in piles: count[x] += 1

        # Perform pile-halving
        for _ in range(k):
            count[-1] -= 1
            count[len(count) // 2] += 1

            # Remove empty piles from top, to ensure top pile has any stones
            while count[-1] == 0: count.pop()
        
        # Count remainder
        return sum(i * count[i] for i in range(len(count)))
