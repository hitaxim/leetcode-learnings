class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(postorder.pop())
        if root.val != preorder[-1]:
            root.right = self.constructFromPrePost(preorder, postorder)
        if root.val != preorder[-1]:
            root.left = self.constructFromPrePost(preorder, postorder)
        preorder.pop()
        return root
