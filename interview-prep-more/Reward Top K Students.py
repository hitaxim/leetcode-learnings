class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positiveSet = set(positive_feedback)
        negativeSet = set(negative_feedback)

        heap = []

        for i, r in enumerate(report):
            score = 0
            for word in r.split(" "):
                if word in positiveSet: score += 3
                if word in negativeSet: score -= 1

            if len(heap) < k:
                heapq.heappush(heap, (score, -student_id[i]))
            elif heap[0][0] < score or (heap[0][0] == score and -heap[0][1] > student_id[i]):
                heapq.heappop(heap)
                heapq.heappush(heap, (score, -student_id[i]))

        return [-x[1] for x in sorted(heap, reverse = True)]            
