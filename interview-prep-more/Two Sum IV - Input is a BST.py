from collections import deque
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if(k - node.val in seen):
                return True
            else:
                seen.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
