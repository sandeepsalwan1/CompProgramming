# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # brute
        return self.dfs(root)

    def dfs(self, root):
        if not root: return True
        left = self.maxHeight(root.left)
        right = self.maxHeight(root.right)
        if abs(right-left) > 1: return False
        # sub = (self.isBalanced(root.left))
        return self.dfs(root.left) and self.dfs(root.right)


    def maxHeight(self, root):
        if not root: return 0 
        return 1+ max(self.maxHeight(root.left), self.maxHeight(root.right)) 

        # all the functions 
        # 
        #max height