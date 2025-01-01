"""
class Solution:
  def findPermutation(self, nums: List[int]) -> List[int]:
    n = len(nums)
    bestPick = [[0] * (1 << n) for _ in range(n)]  # Initialize the bestPick array

    @functools.lru_cache(None)  # Use LRU cache for memoization
    def getScore(last: int, mask: int) -> int:
      if mask.bit_count() == len(nums):  # Base case: all numbers are chosen
        return abs(last - nums[0])

      minScore = math.inf
      for i in range(1, len(nums)):
        if mask >> i & 1:  # Skip if this number is already chosen
          continue
        nextMinScore = abs(last - nums[i]) + getScore(i, mask | (1 << i))
        if nextMinScore < minScore:  # Update minimum score and best pick
          minScore = nextMinScore
          bestPick[last][mask] = i

      return minScore

    getScore(0, 1)  # Start the recursion with the first element chosen
    return self._construct(bestPick)  # Construct the result permutation

  def _construct(self, bestPick: List[List[int]]) -> List[int]:
    ans = []
    last = 0
    mask = 1
    for _ in range(len(bestPick)):  # Backtrack to build the optimal permutation
      ans.append(last)
      last = bestPick[last][mask]
      mask |= 1 << last
    return ans  # Return the constructed permutation
    """
    
class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [[[-1, 1e9] for i in range(1<<(n-1))] for j in range((n - 1))]
        for i in range(n-1): # take i + 1
            dp[i][1<<i] = [-1, abs(i+1-nums[0])]
        for k in range(1 << (n-1)):
            for j in range(n-1):
                if k & (1<<j):
                    for i in range(n-1):
                        if i == j:
                            continue
                        if k & (1<<i):
                            if dp[i][k ^ (1<<j)][1] + abs(j + 1 - nums[i+1]) < dp[j][k][1]:
                                dp[j][k] = [i, dp[i][k ^ (1<<j)][1] + abs(j+1 - nums[i+1])]
        st = -1
        stsc = 1e9
        for i in range(n-1):
            if dp[i][-1][1] + abs(-nums[i+1]) < stsc:
                st = i
                stsc = dp[i][(1<<(n-1)) - 1][1] + abs(-nums[i+1])
        ans = [0]
        pre = st
        nowmask = (1<<(n-1)) - 1
        while pre != -1:
            ans.append(pre+1)
            p = pre
            pre = dp[pre][nowmask][0]
            nowmask ^= 1<<p
        return ans
