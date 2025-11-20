# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def dfs(cur):
            if not cur:
                return 0
            leftPath, rightPath = max(dfs(cur.left),0), max(dfs(cur.right),0)
            # val = cur.val + max(leftPath, rightPath)
            # val2 = cur.val + leftPath+ rightPath
            # val3 = max(val,val2)
            takeBoth = cur.val + leftPath+ rightPath
            takeOne = cur.val + max(leftPath, rightPath,0)
            self.res = max(takeBoth ,self.res)
            # dfs(cur.left)
            # dfs(cur.right)
            # print(cu /r.val)
            return takeOne

        dfs(root)
        return self.res


