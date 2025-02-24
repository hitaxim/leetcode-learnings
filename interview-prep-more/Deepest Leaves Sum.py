# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root,level):
            if not root:
                return
            d[level]+=root.val
            dfs(root.left,level+1)
            dfs(root.right,level+1)
        
        d=defaultdict(int)
        dfs(root,0)
        
        mx=max(d)
        return d[mx]
       
