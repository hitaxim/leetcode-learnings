class BinarySearch:
    def find_h_index(self, citations):
        n = len(citations)
        low, high = 0, n - 1
        while low <= high:
            mid = low + (high - low) // 2
            if citations[mid] >= n - mid:
                high = mid - 1
            else:
                low = mid + 1
        return n - low

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return BinarySearch().find_h_index(citations)


"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_citation = max(citations)
        counts = [0] * (max_citation + 1)
        
        # Step 1: Count the number of papers for each citation count
        for citation in citations:
            counts[citation] += 1
        
        total_papers = 0
        
        # Step 2: Calculate how many papers have at least `h` citations
        for h in range(max_citation, -1, -1):
            total_papers += counts[h]
            if total_papers >= h:
                return h
        
        return 0  # Fallback

"""
