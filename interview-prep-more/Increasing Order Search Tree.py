class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ptr = TreeNode()
        res = ptr

        def inorder(node):
            nonlocal ptr
            if not node:
                return
            
            inorder(node.left)
            ptr.right = TreeNode(node.val)
            ptr = ptr.right
            inorder(node.right)

        inorder(root)
        return res.right
