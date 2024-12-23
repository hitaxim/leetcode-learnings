# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:                                                            
    def minimumOperations(self, root: TreeNode) -> int:                     
        ans, queue, level = 0, [root],[]                                    
        while queue :                                                       
            for node in queue:                                              
                    if node:  level.extend([node.left, node.right])        
            arr = [(v,i) for i,v in enumerate([c.val for c in level if c])] 
            idx = [i for _,i in sorted(arr)]                                
            for i in range(len(idx)):                                       
                while (idx[i] != i):                                        
                    j = idx[i]                                              
                    idx[i], idx[j] = idx[j], idx[i]
                    ans += 1

            queue, level = level, []
        
        return ans
