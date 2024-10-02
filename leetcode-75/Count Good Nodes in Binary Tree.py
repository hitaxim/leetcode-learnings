class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: 
            return 0

        total = 0
        visited = [(root, float('-inf'))]
        
        while visited: 
            node, max_val = visited.pop()
            if node.val >= max_val: 
                total += 1
                max_val = node.val
            
            if node.left: 
                visited.append((node.left, max_val))
            if node.right: 
                visited.append((node.right, max_val))
        
        return total
