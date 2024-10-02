class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sums = defaultdict(int) # hmap
        sums[0] = 1

        def dfs(root, total):
            count = 0
            if root: 
                total += root.val
                count = sums[total-targetSum]
                sums[total] += 1

                count += dfs(root.left, total) + dfs(root.right, total)
                sums[total] -= 1
            return count
        return dfs(root, 0)
