class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        char_count = {"a": a, "b": b, "c": c}
        ans = ""

        while char_count: 
            sorted_chars = sorted(char_count.items(), key = lambda x: x[1], reverse = True)
            max_char, max_count = sorted_chars[0]
            if len(ans) >= 2 and ans[-1] == ans[-2] == max_char: 
                if len(sorted_chars) > 1 and sorted_chars[1][1] > 0:
                    max_char = sorted_chars[1][0]
                else: 
                    break
            
            if max_count <= 0: 
                break
            
            ans += max_char
            char_count[max_char] -= 1
        return ans

"""
import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # time complexity: O(a+b+c)
        # space complexity: O(a+b+c)

        max_heap = []
        if a > 0: max_heap.append((-a, 'a'))
        if b > 0: max_heap.append((-b, 'b'))
        if c > 0: max_heap.append((-c, 'c'))
        heapq.heapify(max_heap)

        curr = ''
        while max_heap:
            freq1, ch1 = heappop(max_heap)
            if not curr or curr[-1] != ch1 or (curr[-1] == ch1 and (len(curr)==1 or curr[-2] != ch1)):
                curr += ch1
                if freq1 + 1 != 0:
                    heappush(max_heap, (freq1+1, ch1))
            else:
                if not max_heap: return curr
                freq2, ch2 = heappop(max_heap)
                
                curr += ch2
                if freq2 + 1 != 0:
                    heappush(max_heap, (freq2+1, ch2))
        
                heappush(max_heap, (freq1, ch1))
        return curr
"""
