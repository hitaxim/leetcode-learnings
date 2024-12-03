# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)

        res = []
        while q: 
            num = len(q)
            avg = []
            for i in range(len(q)):
                x = q.popleft()
                if x: 
                    avg.append(x.val)
                    q.append(x.left)
                    q.append(x.right)
            if avg: 
                res.append(sum(avg)/len(avg))
        
        return res 
