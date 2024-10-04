class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs1 = []
        leafs2 = []
        def inorder(root, result):
            if not root:
                return
            if not root.right and not root.left:
                result.append(root.val)
                return
            inorder(root.left, result)
            inorder(root.right, result)
        inorder(root1, leafs1)
        inorder(root2, leafs2)
        print(leafs1, leafs2)
        return leafs1 == leafs2
