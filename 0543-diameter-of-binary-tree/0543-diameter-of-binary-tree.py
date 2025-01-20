# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
root


depth 1 = 0 

everytime we iterate we add 1 to depth 
maxDiam = 0
dfs params: curr, diam

everytime we iterate to left/right we'll add 1 to diam
every iteration we'll compare maxDiam with curr depth

'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiam = 0
        # height = max(l,r) + 1
        def dfs(curr):
            if not curr: return -1
            left = dfs(curr.left)
            right = dfs(curr.right) 
            diam = left + right+ 2 
            self.maxDiam = max(self.maxDiam, diam)
            return 1+ max(left, right)
        dfs(root)
        return self.maxDiam


        dfs(root,0)
        return self.maxDiam