class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        ans = [0] * k
        
        for x in arr:
            rem = (x % k + k) % k
            ans[rem] += 1

        if ans[0] % 2 != 0:
            return False

        for i in range(1, k): 
            if ans[i] != ans[k-i]:
                return False
        return True
