class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Use as a stack
        stack1 = []
        n = len(temperatures)
        ans = [0] * n

        for i in range(n):
            while stack1 and temperatures[i] > temperatures[stack1[-1]]:
                prev_index = stack1.pop()
                ans[prev_index] = i - prev_index
            stack1.append(i)
        return ans
