# Definition for a binary tree node.
        
# if not root: return True
# return  dfs(root) and self.isValidBST(root.left) and self.isValidBST(root.right) 

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        # dfs  O(n) 
        # space O(log n)
        # node left less than curr
        # node right greater than curr

        
    #         5 
    #      1       4
    #           3     6
    #  l, 5      5, r (inf)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr, l, r):
            if not curr: return True
            if curr.val <= l or curr.val >= r: return False
            return dfs(curr.left, l, curr.val) and dfs(curr.right, curr.val, r)
        return dfs(root, float('-inf'), float('inf'))





















        # def dfs(curr,l,r):
        #     if not curr: return True
        #     if curr.val <= l or curr.val >= r: return False
        #     return dfs(curr.left, l, curr.val) and dfs(curr.right, curr.val, r)
        # return dfs(root, float('-inf'), float('inf'))








        # def dfs(curr, l, r):
        #     if not curr: return True 
        #     if curr.val <= l or curr.val >= r : return False
        #     return dfs(curr.left,l, curr.val) and dfs(curr.right, curr.val, r)

        # return dfs(root, float('-inf'), float('inf'))

