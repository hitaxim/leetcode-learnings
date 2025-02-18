class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def helper(p, q):
            if not p:
                return False
            if isSameTree(p, q):
                return True
            return helper(p.left, q) or helper(p.right, q)

        return helper(root, subRoot)
