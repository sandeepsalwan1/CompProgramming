# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




    #       3
    #     1   4
    #   3    1  5



class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs and check at every iteration if greater than currMax
        if not root: return 0
        self.res = 0
        def dfs(curr,currMax):
            if not curr: return 
            if curr.val >= currMax: self.res +=1
            # newMax = max(currMax, curr.val)
            dfs(curr.left, max(currMax, curr.val))
            dfs(curr.right, max(currMax, curr.val))

        dfs(root,root.val)
        return self.res
