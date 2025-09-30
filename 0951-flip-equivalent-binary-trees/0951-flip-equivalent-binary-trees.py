# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sameTree(self, p,q):
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return self.sameTree(p.left, q.left) and  self.sameTree(p.right, q.right)

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        if not root1 or not root2:
            return not root2 and not root1
        if root1.val != root2.val: return False

        case1 =  self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right)
        case2 =  self.flipEquiv(root1.left,root2.right) and self.flipEquiv(root1.right,root2.left)

        return case1 or case2

        if self.sameTree(root1,root2): return True

        def dfs(curr,ptr):
            if self.sameTree(ptr,root2): return True

            if not curr: return False
            curr.left, curr.right = curr.right, curr.left 
            if self.sameTree(ptr,root2) or dfs(curr.left,ptr) or dfs(curr.right,ptr): return True
            curr.left, curr.right = curr.right, curr.left 
            return dfs(curr.left,ptr) or dfs(curr.right,ptr)
        return True if dfs(root1, root1) else False
            
