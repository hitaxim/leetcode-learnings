class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = n * 2 - 1
        result_sequence = [0] * size
        is_number_used = [0] * (n + 1)

        def backtracking(i):
            if i == size:
                return True
            if result_sequence[i] != 0:
                return backtracking(i + 1)

            for num in reversed(range(1, n + 1)):
                if is_number_used[num]:
                    continue

                is_number_used[num] = 1
                result_sequence[i] = num

                if num == 1:
                    if backtracking(i + 1):
                        return True
                elif i + num < size and result_sequence[i + num] == 0:
                    result_sequence[i + num] = num
                    if backtracking(i + 1):
                        return True
                    result_sequence[i + num] = 0
                is_number_used[num] = 0
                result_sequence[i] = 0
            return False

        backtracking(0)
        return result_sequence

"""
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        def backtrack(idx1 = 0): 

            if not unseen: return True

            if ans[idx1]: return backtrack(idx1+1)

            for num in reversed(range(1,n+1)):

                idx2 = idx1 + num if num != 1 else idx1

                if num in unseen and idx2 < n+n-1 and not ans[idx2]:
                    ans[idx1] = ans[idx2] = num
                    unseen.remove(num)

                    if backtrack(idx1+1): return True
                    ans[idx1] = ans[idx2] = 0
                    unseen.add(num)

            return False

        ans, unseen = [0]*(n+n-1), set(range(1,n+1))

        backtrack()

        return ans

"""
