class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        m = defaultdict(list)

        for i, n in enumerate(nums):
            sum_of_digit = 0
            while n > 0:
                digit = n % 10
                sum_of_digit += digit
                n //= 10

            heapq.heappush(m[sum_of_digit], -1 * nums[i])

        res = -1
        for v in m.values():
            if len(v) >= 2:
                n1 = -1 * heapq.heappop(v)
                n2 = -1 * heapq.heappop(v)

                res = max(res, n1 + n2)
        
        return res


"""
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = {}
        ans = -1
        for num in nums:
            curr = sum(int(digit) for digit in str(num)) # get sum of digits
            if curr in dic:
                ans = max(ans, num + dic[curr])
                dic[curr] = max(dic[curr], num)
            else:
                dic[curr] = num
        return ans
"""      
