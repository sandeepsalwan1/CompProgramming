# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res =0
        def dfs(cur,curNum):
            if not cur:
                return
            # path.append(str(cur.val))
            curNum = (curNum *10)+cur.val
            if not cur.left and not cur.right:
                self.res += curNum
            dfs(cur.left, curNum)
            dfs(cur.right, curNum)

            
        dfs(root,0)
        return self.res