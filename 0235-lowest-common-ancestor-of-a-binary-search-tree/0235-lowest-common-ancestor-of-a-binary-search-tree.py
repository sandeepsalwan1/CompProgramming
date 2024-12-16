# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #run dfs on every attempt
        if p.val <= root.val < q.val  or q.val <= root.val < p.val:
            return root
        if p.val == root.val or q.val == root.val: return root
        if p.val < root.val  and q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val  and q.val > root.val: 
            return self.lowestCommonAncestor(root.right, p, q)

        # count = 0
        # def dfs(root):
        #     if not root: return False
        #     if root.val == count+=1      



        # #if root = q count +=1 count =2 then return 
        # #for to call all the nodes and count = 0  if return true return i 