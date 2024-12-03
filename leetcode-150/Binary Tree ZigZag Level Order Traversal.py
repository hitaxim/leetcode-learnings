# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        my_dict = defaultdict(list)

        def dfs(root, height):
            if not root:
                return
            
            height += 1
            my_dict[height].append(root.val)

            dfs(root.left, height)
            dfs(root.right, height)

            return my_dict
        
        dfs(root, 0)
        result = []
        if my_dict:
            for k, v in sorted(my_dict.items()):
                if k % 2 == 0:
                    v.reverse()
                result.append(v)
        return result
