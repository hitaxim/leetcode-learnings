class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_count = Counter(words)

        heap = [(-count, word) for word, count in freq_count.items()]

        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]

  class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Step 1: Count the frequency of each word
        counts = Counter(words)
        
        # Step 2: Sort words by frequency and lexicographical order
        sorted_words = sorted(counts.keys(), key=lambda word: (-counts[word], word))
        
        # Step 3: Return the top k frequent words
        return sorted_words[:k]
