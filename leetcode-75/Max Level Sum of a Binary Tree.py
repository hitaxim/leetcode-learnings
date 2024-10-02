class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        minLevel = 1
        maxSum = float('-inf')

        queue = deque()
        queue.append(root)

        level = 1

        while queue:
            levelSum = 0
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                levelSum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if levelSum > maxSum:
                maxSum = levelSum
                minLevel = level
            level += 1
        return minLevel
