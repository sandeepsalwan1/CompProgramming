# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(cur, subRoot):
            if not cur and not subRoot: return True
            
            # if s and t and s.val == t.val:
            #     return  sameTree(cur.left, subRoot.left) and sameTree(cur.right, subRoot.
            # return False
            if cur and subRoot and cur.val != subRoot.val:
                return False
            if cur and subRoot:
                return  sameTree(cur.left, subRoot.left) and   sameTree(cur.right, subRoot.right)
    
        if not root: return False
        if not subRoot: return True
        left = sameTree(root.left, subRoot)
        right = sameTree(root.right, subRoot)
        return left or right
        return dfs(root.left,subRoot.left ) and dfs(root.right,subRoot.right)

