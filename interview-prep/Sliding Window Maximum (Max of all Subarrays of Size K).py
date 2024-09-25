def printMax(arr, N, K):
    max = 0

    for i in range(N - K + 1):
        max = arr[i]
        for j in range(1, K):
            if arr[i + j] > max:
                max = arr[i + j]
        print(str(max) + " ", end="")
ORRRRRR

import heapq

def max_sliding_window(arr, k):
    ans = []
    heap = []

    # Initialize the heap with the first k elements
    for i in range(k):
        heapq.heappush(heap, (-arr[i], i))

    # The maximum element in the first window
    ans.append(-heap[0][0])

    # Process the remaining elements
    for i in range(k, len(arr)):
        heapq.heappush(heap, (-arr[i], i))

        # Remove elements that are outside the current window
        while heap[0][1] <= i - k:
            heapq.heappop(heap)

        # The maximum element in the current window
        ans.append(-heap[0][0])

    return ans
