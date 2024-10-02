class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return 
        queue = deque([root])
        res = []
        while len(queue) > 0:
            for _ in range(len(queue)):
                node = queue.popleft() 
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            res.append(node.val)
        return res
