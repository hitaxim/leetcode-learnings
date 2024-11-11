class Solution:

    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        nums = strength.copy()
        stack = []
       
        pref = []
       
        dp = [0]*n
        for i in range(n):
            pref.append((pref[-1] if pref else 0) + nums[i])
        
        sm = 0
        
        prefSum = [0]*n
        ans = 0
        for i in range(n):
            prefSum[i] = (i+1)*nums[i] + (prefSum[i-1] if i > 0 else 0)
            while stack and stack[-1][0] >= nums[i]:
                x = stack.pop()
                sm -= x[1] 
            if stack:
                ind = stack[-1][2]
                val = dp[ind] + (pref[i] - pref[ind])*sm
                val += (prefSum[i] - prefSum[ind] - (ind+1)*(pref[i] - pref[ind]))*nums[i]
                dp[i] = val
                ans += val
                stack.append((nums[i], (i-ind)*nums[i], i))
                sm += (i-ind)*nums[i]
            else:
                ans += prefSum[i]*nums[i]
                dp[i] = prefSum[i]*nums[i]
                stack.append((nums[i], (i+1)*nums[i], i))
                sm += (i+1)*nums[i]
        return ans % (10**9 + 7)
