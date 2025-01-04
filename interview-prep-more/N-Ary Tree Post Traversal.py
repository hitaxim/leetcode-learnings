"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: 
            return []
        
        res = []

        def dfs(root):
            for x in root.children:
                dfs(x)
            res.append(root.val)
        
        dfs(root)

        return res
        
